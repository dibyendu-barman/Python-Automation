import csv
import json
from pathlib import Path
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
)

from reportlab.lib import colors

with open("config/device.json") as f:
    config = json.load(f)

with open("data/test_results.csv", newline="") as f:
    rows = list(csv.DictReader(f))

passed = sum(r["result"] == "PASS" for r in rows)
failed = sum(r["result"] == "FAIL" for r in rows)
total = len(rows)
rate = passed / total * 100 if total else 0

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output = Path("reports") / f"validation_report_{timestamp}.pdf"

doc = SimpleDocTemplate(str(output), pagesize=A4)
styles = getSampleStyleSheet()

table_data = [["Test", "Result", "Value"]]
for row in rows:
    table_data.append([row["test"], row["result"], row["value"]])

table = Table(table_data, colWidths=[150, 100, 100])
table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
    ("ALIGN", (1,1), (-1,-1), "CENTER"),
]))

story = [
    # Paragraph(config["project"], styles["Title"]),
    Spacer(1, 6),
    Paragraph(f"Device: {config['device']}", styles["BodyText"]),
    # Paragraph(f"Firmware: {config['firmware']}", styles["BodyText"]),
    Paragraph(f"Execution: {timestamp}", styles["BodyText"]),
    Spacer(1, 8),
    table,
    Spacer(1, 8),
    Paragraph(
        f"Total: {total} | Passed: {passed} | Failed: {failed} | "
        f"Pass Rate: {rate:.1f}% | "
        f"Overall: {'PASS' if failed == 0 else 'FAIL'}",
        styles["Heading2"]
    )
]

doc.build(story)
print("Created:", output)