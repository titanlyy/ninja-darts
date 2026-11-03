#!/usr/bin/env python3
"""Link only Ninja Darts country workbooks to public feeds using authorised gws.

Requires the owner's explicit permission to enable workbook-level external URL
imports. Existing source tabs are preserved. Never changes sharing permissions,
stores credentials, or runs inside GitHub Actions.
"""
import argparse
import json
import subprocess
from pathlib import Path

from phoenix_global import COUNTRIES, ROOT, cc_for

RAW = "https://raw.githubusercontent.com/titanlyy/ninja-darts/main/data/phoenix"


def gws(service, resource, method, params, body=None):
    command = ["gws", service, resource, method, "--params", json.dumps(params)]
    if body is not None:
        command += ["--json", json.dumps(body)]
    result = subprocess.run(command, text=True, capture_output=True, check=True)
    return json.loads(result.stdout)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--allow-external-imports", action="store_true")
    parser.add_argument("--folder", required=True)
    parser.add_argument("--only", default="")
    parser.add_argument("--state", default=str(ROOT.parent / "phoenix-drive-sync.json"))
    args = parser.parse_args()
    if not args.allow_external_imports:
        raise ValueError("Obtain owner approval for workbook external-URL imports first")
    state_path = Path(args.state)
    state = json.loads(state_path.read_text()) if state_path.exists() else {}
    files, token = [], None
    while True:
        params = {"q": f"'{args.folder}' in parents and trashed = false",
                  "fields": "files(id,name,mimeType),nextPageToken", "pageSize": 100}
        if token:
            params["pageToken"] = token
        result = gws("drive", "files", "list", params)
        files += result.get("files", [])
        token = result.get("nextPageToken")
        if not token:
            break
    aliases = {"ae": ["UAE"], "hk": ["Hong Kong - Macau"]}
    routes = args.only.split(",") if args.only else [r for r, _ in COUNTRIES]
    for route, name in COUNTRIES:
        if route not in routes:
            continue
        cc = cc_for(route)
        names = [name] + aliases.get(route, [])
        titles = {f"{prefix} - {n}".casefold() for prefix in ("DARTSLIVE Venues", "Darts Venues") for n in names}
        matches = [f for f in files if f["mimeType"] == "application/vnd.google-apps.spreadsheet" and f["name"].casefold() in titles]
        if len(matches) > 1:
            raise ValueError(f"Ambiguous workbook for {name}; refusing to overwrite")
        workbook = matches[0] if matches else gws("drive", "files", "create", {
            "fields": "id,name,webViewLink",
        }, {"name": f"Darts Venues - {name}", "mimeType": "application/vnd.google-apps.spreadsheet",
            "parents": [args.folder],
            "description": "Ninja Darts public Phoenix feeds and collection audit. Pending/unavailable does not mean zero installations. Original DARTSLIVE tabs, where present, are preserved."})
        sid = workbook["id"]
        schema = gws("sheets", "spreadsheets", "get", {
            "spreadsheetId": sid, "fields": "sheets.properties,properties.importFunctionsExternalUrlAccessAllowed",
        })
        existing = {s["properties"]["title"]: s["properties"]["sheetId"] for s in schema.get("sheets", [])}
        requests = []
        for title in ("Phoenix Live", "Collection status"):
            if title not in existing:
                requests.append({"addSheet": {"properties": {"title": title, **({"index": 0} if title == "Phoenix Live" and not matches else {}), "gridProperties": {
                    "columnCount": 14 if title == "Phoenix Live" else 10,
                    "rowCount": (20000 if cc in {"jp", "kr", "fr", "us"} else 3000) if title == "Phoenix Live" else 30,
                    "frozenRowCount": 1 if title == "Phoenix Live" else 0,
                }}}})
        if workbook["name"].startswith("Darts Venues - ") and "Phoenix Live" in existing:
            requests.append({"updateSheetProperties": {
                "properties": {"sheetId": existing["Phoenix Live"], "index": 0},
                "fields": "index",
            }})
        if not schema.get("properties", {}).get("importFunctionsExternalUrlAccessAllowed"):
            requests.append({"updateSpreadsheetProperties": {
                "properties": {"importFunctionsExternalUrlAccessAllowed": True},
                "fields": "importFunctionsExternalUrlAccessAllowed",
            }})
        if requests:
            gws("sheets", "spreadsheets", "batchUpdate", {"spreadsheetId": sid}, {"requests": requests})
        # RAW for text; USER_ENTERED is deliberately limited to our two trusted formulas.
        feed_formula = f'=IFERROR(IMPORTDATA("{RAW}/{cc}.csv"),"Feed pending or temporarily unavailable. See Collection status.")'
        status_formula = f'=QUERY(IMPORTDATA("{RAW}/coverage.csv"),"select * where Col1 = \'{cc}\'",1)'
        subprocess.run(["gws", "sheets", "spreadsheets", "values", "batchUpdate",
                        "--params", json.dumps({"spreadsheetId": sid}),
                        "--json", json.dumps({"valueInputOption": "USER_ENTERED", "data": [
                            {"range": "'Phoenix Live'!A1", "values": [[feed_formula]]},
                            {"range": "'Collection status'!A3", "values": [[status_formula]]},
                        ]})], text=True, capture_output=True, check=True)
        subprocess.run(["gws", "sheets", "spreadsheets", "values", "batchUpdate",
                        "--params", json.dumps({"spreadsheetId": sid}),
                        "--json", json.dumps({"valueInputOption": "RAW", "data": [
                            {"range": "'Collection status'!A1", "values": [[f"{name}: Phoenix collection audit"]]},
                            {"range": "'Collection status'!A6", "values": [
                                ["Pending/unavailable/failed does not mean zero machines. Map eligibility flags exclude invalid pins and held access-review records."],
                                ["Source coordinates and opening/access details are not independently verified. Listings may be outdated or duplicate another provider's venue."],
                                ["Google controls IMPORTDATA refresh timing; this is not an instant real-time feed."],
                                ["https://github.com/titanlyy/ninja-darts/blob/main/docs/PHOENIX_COVERAGE.md"],
                            ]},
                        ]})], text=True, capture_output=True, check=True)
        state[cc] = {"id": sid, "name": workbook["name"],
                     "url": f"https://docs.google.com/spreadsheets/d/{sid}/edit",
                     "live_feed": f"{RAW}/{cc}.csv"}
        state_path.write_text(json.dumps(state, indent=2))
        print(f"{cc}: {workbook['name']} {sid} linked", flush=True)


if __name__ == "__main__":
    main()
