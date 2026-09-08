from datetime import datetime
from pathlib import Path
from openpyxl import Workbook

report_dir = Path("reports")
report_dir.mkdir(exist_ok=True)

now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

results = [
 ("Voltage", "PASS", 3.31),
 ("Current", "PASS", 0.42),
 ("Temperature", "FAIL", 52.0),
 ("UART", "PASS", 1),
]

passed = sum(r[1] == "PASS" for r in results)
failed = len(results) - passed

rate = passed / len(results) * 100

text_report = (
    "AUTOMATED TEST REPORT\n"
    "=====================\n"
    f"Execution: {now}\n"
    f"Total: {len(results)}\n"
    f"Passed: {passed}\n"
    f"Failed: {failed}\n"
    f"Pass Rate: {rate:.1f}%\n"
    f"Overall: {'PASS' if failed == 0 else 'FAIL'}\n"
)

txt = report_dir / f"test_report_{now}.txt"
txt.write_text(text_report)

wb = Workbook()
ws = wb.active
ws.title = "Results"
ws.append(["Test", "Result", "Value"])
for row in results:
    ws.append(row)
xlsx = report_dir / f"test_report_{now}.xlsx"
wb.save(xlsx)

print(text_report)
print("Generated:", txt)
print("Generated:", xlsx)