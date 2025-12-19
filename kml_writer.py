def write_kml(points):
    with open("stress_crops.kml", "w") as f:
        f.write("""<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2"><Document>
""")
        for lat, lon, conf in points:
            f.write(f"""
<Placemark>
  <name>Stress Crop ({conf})</name>
  <Point><coordinates>{lon},{lat},0</coordinates></Point>
</Placemark>
""")
        f.write("</Document></kml>")
