import csv
from pathlib import Path

Path("data").mkdir(exist_ok=True)

with open("data/results.csv", "w", newline="") as file:
 writer = csv.DictWriter(
 file, fieldnames=["device", "test", "result", "value"]
 )

 writer.writeheader()
 writer.writerows([
 {"device":"ESP32","test":"Voltage","result":"PASS","value":"3.31"},
 {"device":"ESP32","test":"Current","result":"FAIL","value":"0.42"},
 {"device":"ESP32","test":"Temperature","result":"FAIL","value":"52.0"},
 ])

with open("data/results.csv", newline="") as file:
 rows = list(csv.DictReader(file))

passed = sum(row["result"] == "PASS" for row in rows)
failed = sum(row["result"] == "FAIL" for row in rows)

print("Total:", len(rows))
print("Passed:", passed)
print("Failed:", failed)