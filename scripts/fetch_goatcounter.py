import os
import json
import requests

# -------------------------
# CONFIG
# -------------------------
SITE = "hoanganhle"
API_KEY = os.environ["GOATCOUNTER_API_KEY"]

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

# -------------------------
# FLAG HELPER
# -------------------------
def country_to_flag(country_code):
    """
    Convert ISO country code to emoji flag.
    Example: KR -> 🇰🇷
    """
    if not country_code or len(country_code) != 2:
        return "🌍"

    return chr(ord(country_code[0].upper()) + 127397) + \
           chr(ord(country_code[1].upper()) + 127397)


# -------------------------
# FETCH TOTAL VISITS
# -------------------------
total_url = f"https://{SITE}.goatcounter.com/api/v0/stats/total"

response = requests.get(total_url, headers=headers)
response.raise_for_status()

total_data = response.json()
total_visits = total_data.get("count", 0)

# # -------------------------
# # FETCH COUNTRY STATS
# # -------------------------
# country_url = f"https://{SITE}.goatcounter.com/api/v0/stats/hits"

# params = {
#     "by": "country"
# }

# top_countries = []

# try:
#     response = requests.get(
#         country_url,
#         headers=headers,
#         params=params
#     )
#     response.raise_for_status()

#     country_data = response.json()

#     hits = country_data.get("hits", [])

#     total_country_hits = sum(h.get("count", 0) for h in hits)

#     for h in sorted(
#         hits,
#         key=lambda x: x.get("count", 0),
#         reverse=True
#     )[:3]:

#         code = h.get("country", "")
#         count = h.get("count", 0)

#         percent = (
#             round(100 * count / total_country_hits)
#             if total_country_hits > 0 else 0
#         )

#         top_countries.append({
#             "flag": country_to_flag(code),
#             "country": code,
#             "percent": percent
#         })


country_url = f"https://{SITE}.goatcounter.com/api/v0/stats/hits"

top_countries = []

try:

    response = requests.get(

        country_url,

        headers=headers

    )

    print("Status:", response.status_code)

    print("URL:", response.url)

    print("Response:")

    print(response.text[:3000])

except Exception as e:
    print("Country stats unavailable:", e)

# -------------------------
# SAVE JSON
# -------------------------
visitor_stats = {
    "total": total_visits,
    "countries": top_countries,
    "monthly": 0
}

os.makedirs("_data", exist_ok=True)

with open("_data/visitor_stats.json", "w") as f:
    json.dump(visitor_stats, f, indent=2)

print("Updated visitor_stats.json")


# import os
# import json
# import requests

# SITE = "hoanganhle"
# API_KEY = os.environ["GOATCOUNTER_API_KEY"]

# headers = {
#     "Authorization": f"Bearer {API_KEY}"
# }

# # Use the stats endpoint
# url = f"https://{SITE}.goatcounter.com/api/v0/stats/total"

# response = requests.get(url, headers=headers)

# print("Status code:", response.status_code)
# print(response.text)

# response.raise_for_status()

# data = response.json()

# # Try to find a sensible total
# total_visits = data.get("total", 0)

# visitor_stats = {
#     "total": total_visits,
#     "countries": [],
#     "monthly": 0
# }

# os.makedirs("_data", exist_ok=True)

# with open("_data/visitor_stats.json", "w") as f:
#     json.dump(visitor_stats, f, indent=2)

# print("Updated visitor_stats.json")