import json

with open("config/device.json") as file:
    config = json.load(file)

device = config["device"]
limits = config["limits"]

measurements = {
    "voltage": 3.31,
    "temperature": 38.5
}

voltage_ok = limits["voltage_min"] <= measurements["voltage"] <= limits["voltage_max"]
temperature_ok = measurements["temperature"] <= limits["temperature_max"]

print("DEVICE:", device)
print("Voltage Test :", "PASS" if voltage_ok else "FAIL")
print("Temperature Test:", "PASS" if temperature_ok else "FAIL")