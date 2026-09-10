import requests
from pathlib import Path

url = "https://example.com/"
response = requests.get(url, timeout=10)
response.raise_for_status()
Path("data").mkdir(exist_ok=True)

output = Path("data/example.html")
output.write_text(response.text, encoding="utf-8")

print("Downloaded:", output)
print("Bytes:", output.stat().st_size)