"""Choose only bounded, checkpointed runtime-budget continuations, never blocks."""
import json
import re
import sys
from pathlib import Path


def continuation_routes(manifest):
    countries = manifest["countries"]
    if any(country.get("status") == "blocked" for country in countries):
        return []
    routes = []
    for country in countries:
        if country.get("status") != "partial":
            continue
        if country.get("continuation_attempt", 0) >= 3:
            continue
        # Do not reinterpret unrelated partial/failure states as timed resumptions.
        if not country.get("note", "").startswith("Checkpointed before runner time limit;"):
            continue
        code = country["country_code"]
        if not re.fullmatch("[a-z]{2}", code) or code == "sg":
            continue
        route = "uk" if code == "gb" else code
        if route not in routes:
            routes.append(route)
    return routes


if __name__ == "__main__":
    print(json.dumps(continuation_routes(json.loads(Path(sys.argv[1]).read_text()))))
