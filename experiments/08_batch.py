from pathlib import Path
import shutil

input_dir = Path("input_data")
output_dir = Path("processed_data")

input_dir.mkdir(exist_ok=True)
output_dir.mkdir(exist_ok=True)

for name in ["test_01.log", "test_02.log", "notes.txt"]:
    file = input_dir / name
    if not file.exists():
        file.write_text("PASS\n")

processed = 0

for file in input_dir.glob("*.log"):
    destination = output_dir / file.name
    try:
        shutil.copy2(file, destination)
        processed += 1
        print("Processed:", file.name)
    except OSError as error:
        print("ERROR:", file.name, error)
    
print("Total processed:", processed)