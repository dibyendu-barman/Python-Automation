import requests

url = "https://example.com"

try:
    response = requests.get(url, timeout=10)

    print("URL :", url)
    print("Status:", response.status_code)
    print("Type :", response.headers.get("content-type"))
    print("PASS :", response.ok)

except requests.RequestException as error:
    print("Request failed:", error)