from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from pathlib import Path

Path("reports").mkdir(exist_ok=True)

doc = SimpleDocTemplate("reports/engineering_report.pdf", pagesize=A4)
styles = getSampleStyleSheet()

data = [
    ["Test", "Measured", "Limit", "Result"],
    ["Voltage", "3.31 V", "3.20–3.40 V", "PASS"],
    ["Current", "0.42 A", "0.30–0.60 A", "PASS"],
    ["Temperature", "52.0 C", "<= 45 C", "FAIL"],
]

table = Table(data, colWidths=[45, 70, 80, 55])
table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
    ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
    ("ALIGN", (1,1), (-1,-1), "CENTER"),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
]))

story = [
    Paragraph("Engineering Validation Report", styles["Title"]),
    Spacer(1, 10),
    Paragraph("Device: ESP32", styles["BodyText"]),
    Spacer(1, 8),
    table,
]

doc.build(story)
print("Created: reports/engineering_report.pdf")
