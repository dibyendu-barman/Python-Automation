import json

data = {
 "devices": [
    {"name":"ESP32","tests":{"voltage":"PASS","uart":"PASS","temp":"FAIL"}},
    {"name":"STM32","tests":{"voltage":"PASS","uart":"PASS","temp":"PASS"}},
    {"name":"PIC16F877A","tests":{"voltage":"FAIL","uart":"PASS","temp":"PASS"}}
 ]
}

with open("data/devices.json", "w") as f:
    json.dump(data, f, indent=4)

for device in data["devices"]:
    results = list(device["tests"].values())
    passed = results.count("PASS")
    total = len(results)
    rate = passed / total * 100
    print(f"{device['name']:<12} {passed}/{total} {rate:.1f}%")
