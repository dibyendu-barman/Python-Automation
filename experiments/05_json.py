import json
from pathlib import Path

config = {
    "device": "ESP32",
    "interface": "UART",
    "limits": {
        "voltage_min": 3.20,
        "voltage_max": 3.40,
        "temperature_max": 45
    },
    "tests": ["voltage", "temperature", "communication"]
}

Path("config").mkdir(exist_ok=True)

with open("config/device.json", "w") as file:
    json.dump(config, file, indent=4)

with open("config/device.json") as file:
    loaded = json.load(file)

print("Device:", loaded["device"])
print("Interface:", loaded["interface"])
print("Voltage max:", loaded["limits"]["voltage_max"])
print("Tests:", loaded["tests"])
