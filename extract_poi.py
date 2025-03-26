import gpxpy
import json

# Sett filnavnet til din GPX-fil
gpx_file = "Fjellruta_over_Vegglifjell_og_Imingfjell.gpx"

with open(gpx_file, "r", encoding="utf-8") as f:
    gpx = gpxpy.parse(f)

waypoints = []
for wpt in gpx.waypoints:
    waypoints.append({
        "name": wpt.name or "Navnløs",
        "lat": wpt.latitude,
        "lon": wpt.longitude,
        "desc": wpt.description or ""
    })

with open("fjellruta_poi.json", "w", encoding="utf-8") as f:
    json.dump(waypoints, f, indent=2, ensure_ascii=False)

print(f"✅ Laget fjellruta_poi.json med {len(waypoints)} punkter.")
