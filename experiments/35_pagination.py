import requests
import time

base_url = "https://example.com/items?page={}"

all_items = []

for page in range(1, 4):
    url = base_url.format(page)
    print("Requesting:", url)
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        # Replace this with real parsing for an authorized target.
        all_items.append({
        "page": page,
        "status": response.status_code
        })
    
    except requests.RequestException as error:
        print("Error:", error)
 
    time.sleep(1)

print("Pages processed:", len(all_items))
