from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from pathlib import Path

Path("reports").mkdir(exist_ok=True)

def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.drawString(40, 20, "Python Automation Lab")
    canvas.drawRightString(555, 20, f"Page {doc.page}")
    canvas.restoreState()

doc = SimpleDocTemplate(
    "reports/controlled_report.pdf",
    pagesize=A4,
    title="Device Validation Report",
    author="Python Automation Lab"
)

styles = getSampleStyleSheet()
story = [Paragraph("Controlled Validation Report", styles["Title"])]

for i in range(1, 8):
    story += [
        Paragraph(f"Test Section {i}", styles["Heading2"]),
        Paragraph("Automated test evidence and engineering observations.",
        styles["BodyText"]),
        Spacer(1, 20)
 ]

doc.build(story, onFirstPage=footer, onLaterPages=footer)
print("Created: reports/controlled_report.pdf")
