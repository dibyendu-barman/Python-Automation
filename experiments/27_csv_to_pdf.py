import csv
from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table

Path("reports").mkdir(exist_ok=True)

with open("data/test_results.csv", newline="") as f:
     rows = list(csv.DictReader(f))

passed = sum(r["result"] == "PASS" for r in rows)
failed = sum(r["result"] == "FAIL" for r in rows)
rate = passed / len(rows) * 100 if rows else 0

data = [["Device", "Test", "Result", "Value"]]
for row in rows:
    data.append([row["device"], row["test"], row["result"], row["value"]])

doc = SimpleDocTemplate("reports/csv_test_report.pdf", pagesize=A4)
styles = getSampleStyleSheet()

story = [
    Paragraph("CSV Test Results Report", styles["Title"]),
    Spacer(1, 8),
    Paragraph(f"Total: {len(rows)} | PASS: {passed} | FAIL: {failed} | Rate: {rate:.1f}%",
    styles["BodyText"]),
    Spacer(1, 8),
    Table(data)
]

doc.build(story)
print("Created: reports/csv_test_report.pdf")