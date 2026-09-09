from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from pathlib import Path

def build_report(filename, device, firmware, overall):
    doc = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
 
    story = [
        Paragraph("Device Validation Report", styles["Title"]),
        Spacer(1, 8),
        Paragraph(f"Device: {device}", styles["BodyText"]),
        Paragraph(f"Firmware: {firmware}", styles["BodyText"]),
        Spacer(1, 8),
        Paragraph(f"Overall Result: {overall}", styles["Heading2"]),
    ]
    
    doc.build(story)

Path("reports").mkdir(exist_ok=True)
    
build_report(
    "reports/esp32_report.pdf",
    "ESP32",
    "v1.2.0",
    "PASS"
)
    
build_report(
    "reports/stm32_report.pdf",
    "STM32",
    "v2.1.0",
    "FAIL"
)

print("Reports generated.")