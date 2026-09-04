import csv
from pathlib import Path

Path("data").mkdir(exist_ok=True)

rows = [
    ["ESP32","Voltage","PASS","3.31"],
    ["ESP32","Current","PASS","0.42"],
    ["ESP32","Temperature","FAIL","52.0"],
    ["ESP32","UART","PASS","1"],
    ["ESP32","Functional","FAIL","0"],
]

with open("data/test_results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["device","test","result","value"])
    writer.writerows(rows)
with open("data/test_results.csv", newline="") as f:
    data = list(csv.DictReader(f))

passed = [r for r in data if r["result"] == "PASS"]
failed = [r for r in data if r["result"] == "FAIL"]
rate = len(passed) / len(data) * 100

print("Total :", len(data))
print("PASS :", len(passed))
print("FAIL :", len(failed))
print(f"Rate : {rate:.1f}%")