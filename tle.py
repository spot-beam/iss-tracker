# fetches and extrapolates the most recent TLE for the ISS

import requests
from datetime import datetime, timezone

url = "https://celestrak.org/NORAD/elements/stations.txt"

def extract_tle(lines):
    for i in range(len(lines)):
        if lines[i].strip() == "ISS (ZARYA)":
            return lines[i], lines[i+1], lines[i+2]
    raise ValueError("TLE for the International Space Station not found")

response = requests.get(url, timeout=10)
response.raise_for_status()
tle_lines = response.text.splitlines()

name, line1, line2 = extract_tle(tle_lines)
timestamp = datetime.now(timezone.utc).isoformat()

with open("data/iss.tle", "w") as f:
    f.write(f"# fetched_at_utc: {timestamp}\n")
    f.write(name + "\n")
    f.write(line1 + "\n")
    f.write(line2 + "\n")

