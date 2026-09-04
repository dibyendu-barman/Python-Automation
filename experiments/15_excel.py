from openpyxl import Workbook
from pathlib import Path

Path("reports").mkdir(exist_ok=True)

wb = Workbook()
ws = wb.active
ws.title = "Test Results"

headers = ["Device", "Test", "Result", "Value"]
ws.append(headers)

ws.append(["ESP32", "Voltage", "PASS", 3.31])
ws.append(["ESP32", "Current", "PASS", 0.42])
ws.append(["ESP32", "Temperature", "FAIL", 52.0])

wb.save("reports/test_results.xlsx")

print("Created: reports/test_results.xlsx")