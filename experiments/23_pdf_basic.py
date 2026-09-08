from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from pathlib import Path

Path("reports").mkdir(exist_ok=True)

doc = SimpleDocTemplate("reports/test_report.pdf", pagesize=A4)
styles = getSampleStyleSheet()

story = []
story.append(Paragraph("Engineering Test Report", styles["Title"]))
story.append(Spacer(1, 12))
story.append(Paragraph("Device: ESP32", styles["BodyText"]))
story.append(Paragraph("Firmware: v1.2.0", styles["BodyText"]))
story.append(Spacer(1, 8))

story.append(Paragraph("Voltage Test: PASS", styles["BodyText"]))
story.append(Paragraph("Current Test: PASS", styles["BodyText"]))
story.append(Paragraph("Temperature Test: FAIL", styles["BodyText"]))

doc.build(story)
print("Created: reports/test_report.pdf")