#!/usr/bin/env python3
"""
DARTSLIVE Shop Database Scraper (API-based, Multi-Threaded)
============================================================
Fetches clean shop data directly from the DARTSLIVE API.

HOW TO USE:
1. Install Python (https://www.python.org/downloads/) if you haven't
2. Open Terminal (Mac/Linux) or Command Prompt (Windows)
3. Run: pip install requests beautifulsoup4
4. Run: python dartslive_scraper.py
5. Your data will be saved as: dartslive_shops.csv
"""

import requests
from bs4 import BeautifulSoup
import csv
import os
import time
import re
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock

REGIONS = {
    "jp":  "Japan",
    "au":  "Australia",
    "ca":  "Canada",
    "cn":  "China",
    "es":  "España (Spain)",
    "fi":  "Finland",
    "fr":  "France",
    "hk":  "Hong Kong / Macau",
    "id":  "Indonesia",
    "kr":  "Korea",
    "my":  "Malaysia",
    "nz":  "New Zealand",
    "ph":  "Philippines",
    "qa":  "Qatar",
    "sg":  "Singapore",
    "ch":  "Suisse (Switzerland)",
    "tw":  "Taiwan",
    "th":  "Thailand",
    "gb":  "United Kingdom",
    "us":  "USA",
    "ae":  "UAE",
}

BASE_URL    = "https://search.dartslive.com"
API_URL     = "https://search.dartslive.com/api/v1"
MAX_WORKERS = 10
print_lock  = Lock()

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0 Safari/537.36"
    ),
    "Accept": "application/json",
    "Referer": "https://search.dartslive.com/",
}

DAY_MAP = {
    "日曜日": "Sun", "月曜日": "Mon", "火曜日": "Tue",
    "水曜日": "Wed", "木曜日": "Thu", "金曜日": "Fri",
    "土曜日": "Sat", "祝日": "Holiday",
}

def is_venue_website(value):
    """Exclude known corporate footer policy links, not the raw source record."""
    try:
        url = urlparse(value.strip())
        return (url.scheme in {"http", "https"} and bool(url.hostname)
                and not (url.hostname.endswith("segasammy.co.jp")
                         and "socialmediapolicy" in url.path.lower()))
    except (TypeError, ValueError, AttributeError):
        return False

def translate_hours(raw_hours):
    """Convert Japanese day names to English in business hours string."""
    if not raw_hours:
        return ""
    for jp, en in DAY_MAP.items():
        raw_hours = raw_hours.replace(jp, en)
    return raw_hours.strip()

def get_json(url, retries=3):
    """Fetch a URL and return parsed JSON, or None on failure."""
    for attempt in range(retries):
        try:
            resp = requests.get(url, headers=HEADERS, timeout=15)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            with print_lock:
                print(f"    ⚠️  Attempt {attempt+1}/{retries} failed: {url} → {e}")
            time.sleep(2)
    return None

def get_html_soup(url, retries=3):
    """Fetch a URL and return BeautifulSoup for HTML parsing."""
    for attempt in range(retries):
        try:
            resp = requests.get(url, headers={**HEADERS, "Accept": "text/html"}, timeout=15)
            resp.raise_for_status()
            return BeautifulSoup(resp.text, "html.parser")
        except Exception as e:
            with print_lock:
                print(f"    ⚠️  Attempt {attempt+1}/{retries} failed: {url} → {e}")
            time.sleep(2)
    return None

def get_shop_ids_for_region(region_code):
    """Collect all shop IDs from paginated shop listing pages."""
    all_ids = []
    seen    = set()

    def extract_ids_from_soup(soup):
        ids = set()
        for link in soup.select("a[href*='/shop/']"):
            href  = link.get("href", "")
            parts = [p for p in href.split("/") if p]
            if len(parts) >= 3 and parts[1] == "shop":
                ids.add(parts[2])
        return ids

    def fetch_page(page):
        url  = f"{BASE_URL}/{region_code}/shops/?page={page}"
        soup = get_html_soup(url)
        if not soup:
            return page, set()
        return page, extract_ids_from_soup(soup)

    # Page 1 first to confirm the region works
    _, first_ids = fetch_page(1)
    if not first_ids:
        return []
    for sid in first_ids:
        seen.add(sid)
        all_ids.append(sid)

    # Fetch remaining pages in parallel batches
    page = 2
    while True:
        batch   = range(page, page + 20)
        results = {}
        with ThreadPoolExecutor(max_workers=20) as ex:
            futures = {ex.submit(fetch_page, p): p for p in batch}
            for f in as_completed(futures):
                p, ids = f.result()
                results[p] = ids

        found_any = False
        for p in sorted(results):
            for sid in results[p]:
                if sid not in seen:
                    seen.add(sid)
                    all_ids.append(sid)
                    found_any = True

        if not found_any:
            break
        page += 20

    with print_lock:
        print(f"  📋 Found {len(all_ids)} shops in [{region_code}]")
    return all_ids

def scrape_shop(region_code, shop_id):
    """
    Fetch shop data from the DARTSLIVE internal API + basic-info HTML page.
    Returns a clean dict with no JavaScript garbage.
    """
    shop = {
        "region_code":         region_code,
        "region_name":         REGIONS.get(region_code, region_code.upper()),
        "shop_id":             shop_id,
        "shop_name":           "",
        "genre":               "",
        "large_region":        "",
        "medium_region":       "",
        "address":             "",
        "latitude":            "",
        "longitude":           "",
        "nearest_station":     "",
        "business_hours":      "",
        "regular_holidays":    "",
        "budget":              "",
        "equipment":           "",
        "website_url":         "",
        "instagram":           "",
        "x_twitter":           "",
        "facebook":            "",
        "dartslive3_units":    "",
        "dartslive2_units":    "",
        "has_official_league": "",
        "has_campaign":        "",
        "condition_labels":    "",
        "shop_description":    "",
        "atmosphere":          "",
        "payment_methods":     "",
        "other_options":       "",
        "shop_page_url":       f"{BASE_URL}/{region_code}/shop/{shop_id}",
    }

    # ── Primary: internal API ──────────────────────────────────────────────
    api_url  = f"{BASE_URL}/shop/shop-summery/?country_code={region_code}&shop_enc_id={shop_id}"
    api_data = get_json(api_url)

    if api_data and "shop" in api_data:
        s = api_data["shop"]

        shop["shop_name"]   = s.get("shopName", "")
        shop["has_official_league"] = "Yes" if s.get("isLeagueEntry") else "No"
        shop["has_campaign"]        = "Yes" if s.get("hasCampaign") else "No"

        # Machine counts
        machines = s.get("busyMachine", {}).get("machine", {})
        shop["dartslive3_units"] = machines.get("dl3num", "")
        shop["dartslive2_units"] = machines.get("dl2num", "")

        # Location
        loc = s.get("shopLocation", {})
        shop["latitude"]  = loc.get("latitude", "")
        shop["longitude"] = loc.get("longitude", "")

        # Region labels
        region = s.get("region", {})
        shop["large_region"]  = region.get("largeRegion", "")
        shop["medium_region"] = region.get("mediumRegion", "")

        # Condition labels (e.g. "Beginner Friendly", "Non-Smoking")
        labels = s.get("conditionLabels", [])
        shop["condition_labels"] = ", ".join(labels) if labels else ""

        # Genre
        genre_id_map = {
            1: "Darts Bar", 2: "Darts Venue", 3: "Darts Shop",
            4: "Billiards", 5: "Bowling", 6: "Game Centre",
            7: "Internet Cafe", 8: "Karaoke", 9: "Batting Centre", 10: "Other"
        }
        shop["genre"] = genre_id_map.get(s.get("genre"), "")

        # Options (atmosphere, payment, etc.)
        options = s.get("optionGroup", {}).get("optionGroupList", [])
        atmosphere_list = []
        payment_list    = []
        other_list      = []
        for group in options:
            g_name = group.get("group", {}).get("comment", "")
            for opt in group.get("optionList", []):
                comment = opt.get("comment", "")
                if "雰囲気" in g_name or "atmosphere" in g_name.lower() or group.get("group", {}).get("groupId") == 1:
                    atmosphere_list.append(comment)
                elif "決済" in g_name or "payment" in g_name.lower() or group.get("group", {}).get("groupId") == 2:
                    payment_list.append(comment)
                else:
                    other_list.append(comment)

        # Also grab raw atmosphereList IDs if present
        atm_raw = s.get("atmosphere", {}).get("atmosphereList", [])
        atm_id_map = {
            1: "Beginners Welcome", 2: "Easy to Enter Alone", 3: "Good for Practice",
            4: "Lively Atmosphere", 5: "Relaxed", 6: "Good for Dates",
            7: "Good for Groups", 8: "Good for Work Events", 9: "Sports Bar",
            10: "Family Friendly", 11: "Non-Smoking", 12: "No Cover Charge",
            13: "Has Parking", 14: "Open 24H",
        }
        for aid in atm_raw:
            label = atm_id_map.get(aid, f"Atmosphere#{aid}")
            if label not in atmosphere_list:
                atmosphere_list.append(label)

        shop["atmosphere"]       = ", ".join(atmosphere_list)
        shop["payment_methods"]  = ", ".join(payment_list)
        shop["other_options"]    = ", ".join(other_list)

    # ── Secondary: basic-information HTML page (address, hours, social) ───
    info_url  = f"{BASE_URL}/{region_code}/shop/{shop_id}/basic-information"
    info_soup = get_html_soup(info_url)

    if info_soup:
        # Strip all script tags first so we don't accidentally grab JS
        for script in info_soup.find_all("script"):
            script.decompose()

        # Table rows: address, hours, holidays, nearest station, budget, equipment
        # NOTE: pages now contain duplicate rows (hidden mobile/nav blocks), some
        # with empty values — never overwrite a real value with an empty one.
        def set_field(field, value):
            value = value.strip()
            if value and not shop[field]:
                shop[field] = value

        for row in info_soup.find_all("tr"):
            cells = [td.get_text(" ", strip=True) for td in row.find_all(["th", "td"])]
            if len(cells) < 2:
                continue
            key   = cells[0].lower()
            value = " | ".join(cells[1:]).strip()
            # Drop stray "None" tokens that appear in nearest-station rows
            value = " | ".join(
                " ".join(w for w in p.split() if w != "None")
                for p in value.split("|") if p.strip()
            ).strip()

            if "address" in key or "住所" in key:
                set_field("address", value)
            elif "business hours" in key or "営業時間" in key or "hours" in key:
                set_field("business_hours", translate_hours(value))
            elif "regular holiday" in key or "定休日" in key:
                set_field("regular_holidays", value)
            elif "nearest" in key or "station" in key or "最寄" in key:
                set_field("nearest_station", value)
            elif "budget" in key or "予算" in key:
                set_field("budget", value)
            elif "equipment" in key or "設備" in key or "facility" in key:
                set_field("equipment", value)
            elif "url" in key or "website" in key or "web" in key:
                val_lower = value.lower()
                if is_venue_website(value) and "instagram" not in val_lower and "facebook" not in val_lower and "twitter" not in val_lower:
                    set_field("website_url", value)

        # Social media links from <a> tags
        for a in info_soup.find_all("a", href=True):
            href = a["href"]
            if "instagram.com" in href:
                shop["instagram"] = href
            elif "twitter.com" in href or "x.com" in href:
                shop["x_twitter"] = href
            elif "facebook.com" in href:
                shop["facebook"] = href
            elif is_venue_website(href) and not any(s in href for s in ["dartslive", "google", "instagram", "facebook", "twitter", "x.com"]):
                if not shop["website_url"]:
                    shop["website_url"] = href

        # Shop description: first meaningful <p> block (skip short ones)
        for p in info_soup.find_all("p"):
            text = p.get_text(strip=True)
            if len(text) > 40:
                shop["shop_description"] = text[:600]
                break

    return shop

def scrape_region(region_code, region_name):
    """Scrape all shops for one region using a thread pool."""
    with print_lock:
        print(f"\n🌏 Region: {region_name} [{region_code}]")
        print("-" * 40)

    shop_ids = get_shop_ids_for_region(region_code)
    if not shop_ids:
        with print_lock:
            print(f"  ⚠️  No shops found for {region_name}. Skipping.")
        return []

    with print_lock:
        print(f"  🏪 Scraping {len(shop_ids)} shops with {MAX_WORKERS} threads...\n")

    results = []
    done    = 0
    total   = len(shop_ids)

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(scrape_shop, region_code, sid): sid for sid in shop_ids}
        for future in as_completed(futures):
            shop = future.result()
            results.append(shop)
            done += 1
            with print_lock:
                print(f"  [{done}/{total}] ✔ {shop.get('shop_name', 'Unknown')} ({region_code})")

    with print_lock:
        print(f"\n  ✅ Done with {region_name}! ({len(results)} shops)")
    return results

def save_to_csv(shops, filename="dartslive_shops.csv"):
    """Save all shop data to a CSV file."""
    if not shops:
        print("No shops to save.")
        return
    fieldnames = list(shops[0].keys())
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(shops)
    print(f"\n✅ Saved {len(shops)} shops → {filename}")

def main():
    print("=" * 60)
    print("  DARTSLIVE Shop Scraper — API-Based, Multi-Threaded")
    print("=" * 60)

    print("\nAvailable regions:")
    for i, (code, name) in enumerate(REGIONS.items(), 1):
        print(f"  {i:>2}. [{code}] {name}")
    print("  ----")
    print("   0. ALL regions")

    choice = input("\nEnter region number (or 0 for ALL): ").strip()

    if choice == "0":
        selected = list(REGIONS.items())
    else:
        try:
            idx = int(choice) - 1
            region_code, region_name = list(REGIONS.items())[idx]
            selected = [(region_code, region_name)]
        except (ValueError, IndexError):
            print("❌ Invalid choice. Exiting.")
            return

    all_shops  = []
    start_time = time.time()

    for region_code, region_name in selected:
        shops = scrape_region(region_code, region_name)
        all_shops.extend(shops)

    output_file = "dartslive_shops.csv"
    elapsed     = round(time.time() - start_time, 1)

    save_to_csv(all_shops, output_file)

    print("\n" + "=" * 60)
    print(f"  🎯 Scraping complete! Total shops: {len(all_shops)}")
    print(f"  ⏱️  Time taken: {elapsed}s")
    print(f"  📁 File saved: {os.path.abspath(output_file)}")
    print("=" * 60)

if __name__ == "__main__":
    main()
