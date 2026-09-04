from pathlib import Path

log = Path("device.log")
log.write_text(
 "BOOT PASS\n"
 "VOLTAGE PASS\n"
 "CURRENT FAIL\n"
 "TEMPERATURE PASS\n"
)

lines = log.read_text().splitlines()
passed = sum("PASS" in line for line in lines)
failed = sum("FAIL" in line for line in lines)

report = (
 "TEST REPORT\n"
 "-----------\n"
 f"Total : {len(lines)}\n"
 f"Passed: {passed}\n"
 f"Failed: {failed}\n"
)

Path("reports").mkdir(exist_ok=True)
Path("reports/summary.txt").write_text(report)
print(report)