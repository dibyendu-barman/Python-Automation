from pathlib import Path

workspace = Path("automation_workspace")
logs = workspace / "logs"
reports = workspace / "reports"

logs.mkdir(parents=True, exist_ok=True)
reports.mkdir(parents=True, exist_ok=True)

(logs / "device_01.log").write_text("BOOT PASS\nVOLTAGE PASS\n")
(reports / "summary.txt").write_text("Test Summary\n")

print("Workspace:", workspace.resolve())
print("Logs:")
for file in logs.glob("*"):
    print(" -", file.name)
print("Reports:")
for file in reports.glob("*"):
    print(" -", file.name)