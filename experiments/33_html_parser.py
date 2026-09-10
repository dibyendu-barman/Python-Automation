from bs4 import BeautifulSoup
from pathlib import Path

html = '''
<html>
<body>
<h1>Device Test Portal</h1>
<ul>
<li class="test">Voltage - PASS</li>
<li class="test">Current - PASS</li>
<li class="test">Temperature - FAIL</li>
</ul>
</body>
</html>
'''

Path("data/sample.html").write_text(html, encoding="utf-8")

soup = BeautifulSoup(html, "html.parser")

print("Title:", soup.h1.get_text(strip=True))

for item in soup.select(".test"):
    print("Test:", item.get_text(strip=True))