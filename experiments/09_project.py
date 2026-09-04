import csv
import json
import logging
from pathlib import Path

Path("reports").mkdir(exist_ok=True)
Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
 filename="logs/pipeline.log",
 level=logging.INFO,
 format="%(asctime)s | %(levelname)s | %(message)s"
)

with open("config/device.json") as file:
    config = json.load(file)

with open("data/results.csv", newline="") as file:
    rows = list(csv.DictReader(file))

passed = sum(row["result"] == "PASS" for row in rows)
failed = sum(row["result"] == "FAIL" for row in rows)

report = (
    f"DEVICE: {config['device']}\n"
    f"TOTAL : {len(rows)}\n"
    f"PASS : {passed}\n"
    f"FAIL : {failed}\n"
    f"RATE : {passed / len(rows) * 100:.1f}%\n"
    f"OVERALL: {'PASS' if failed == 0 else 'FAIL'}\n"
)

Path("reports/final_report.txt").write_text(report)
logging.info("Processed %d test results", len(rows))
logging.info("Pipeline completed")

print(report)