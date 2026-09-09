from pathlib import Path
from datetime import datetime
import shutil
import zipfile

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
package = Path("reports") / f"validation_package_{timestamp}"
package.mkdir(parents=True, exist_ok=True)

files = [
    Path("reports/csv_test_report.pdf"),
    Path("data/test_results.csv"),
    Path("config/device.json"),
]

for source in files:
    if source.exists():
        shutil.copy2(source, package / source.name)

zip_path = Path("reports") / f"validation_package_{timestamp}.zip"

with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive:
    for file in package.iterdir():
        archive.write(file, arcname=file.name)

print("Package:", package)
print("ZIP:", zip_path)