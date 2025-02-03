import requests
import os
import json
import csv
import time
from time import strftime, gmtime

api_key = "rl_BxonUEYUdN4zs79GjPqiyQMN2"
i = 1
json_folder = "users_json"
csv_folder = "users_csv"

def create_folder(name):
    if not os.path.exists(name):
        os.makedirs(name)
create_folder(json_folder)
create_folder(csv_folder)

while True:
    search_url = f"https://api.stackexchange.com/2.2/users?key={api_key}&page={i}&pagesize=100&order=desc&sort=reputation&site=stackoverflow"
    r = requests.get(search_url, stream=True)
    if r.status_code == 200:
        rec = r.json()
        if "items" not in rec or not rec["items"]:
            print("No more data to fetch. Exiting loop.")
            break
        timestamp = strftime("%Y-%m-%d-%H-%M-%S", gmtime())
        json_filename = os.path.join(json_folder, f"{timestamp}_page_{i}.json")
        csv_filename = os.path.join(csv_folder, f"{timestamp}_page_{i}.csv")
        with open(json_filename, 'w', encoding="utf-8") as f:
            json.dump(rec, f, indent=4)
        print(f"Data for page {i} saved to {json_filename}")
        with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            headers = [
                "user_id", "display_name", "reputation", "location", "website_url",
                "profile_image", "user_type", "link", "account_id", "is_employee",
                "last_modified_date", "last_access_date", "reputation_change_year",
                "reputation_change_quarter", "reputation_change_month", "reputation_change_week",
                "reputation_change_day", "creation_date", "accept_rate",
                "badge_bronze", "badge_silver", "badge_gold", "collective_names"
            ]
            writer.writerow(headers)
            for user in rec["items"]:
                badge_counts = user.get("badge_counts", {})
                badge_bronze = badge_counts.get("bronze", 0)
                badge_silver = badge_counts.get("silver", 0)
                badge_gold = badge_counts.get("gold", 0)
                collectives = user.get("collectives", [])
                collective_names = [c["collective"]["name"] for c in collectives if "collective" in c]
                collective_names_str = ", ".join(collective_names) if collective_names else ""
                writer.writerow([
                    user.get("user_id", ""),
                    user.get("display_name", ""),
                    user.get("reputation", ""),
                    user.get("location", ""),
                    user.get("website_url", ""),
                    user.get("profile_image", ""),
                    user.get("user_type", ""),
                    user.get("link", ""),
                    user.get("account_id", ""),
                    user.get("is_employee", ""),
                    user.get("last_modified_date", ""),
                    user.get("last_access_date", ""),
                    user.get("reputation_change_year", ""),
                    user.get("reputation_change_quarter", ""),
                    user.get("reputation_change_month", ""),
                    user.get("reputation_change_week", ""),
                    user.get("reputation_change_day", ""),
                    user.get("creation_date", ""),
                    user.get("accept_rate", ""),
                    badge_bronze, badge_silver, badge_gold,
                    collective_names_str
                ])
        print(f"Data for page {i} saved to {csv_filename}")
        i += 1
        time.sleep(3)  # Pause between API requests to avoid hitting the rate limit
    else:
        print(f"Failed to fetch data for page {i}. HTTP Status Code: {r.status_code}")
        break
