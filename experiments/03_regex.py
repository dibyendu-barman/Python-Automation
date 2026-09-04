import re

log = '''
[INFO] Device=ESP32 Voltage=3.31V
[INFO] Device=ESP32 Voltage=3.28V
[ERROR] Device=ESP32 Voltage=3.65V
'''

voltages = re.findall(r"Voltage=(\d+\.\d+)V", log)
devices = re.findall(r"Device=(\w+)", log)

print("Devices:", devices)
print("Voltages:", voltages)

for value in voltages:
    voltage = float(value)
    result = "PASS" if 3.20 <= voltage <= 3.40 else "FAIL"
    print(f"{voltage:.2f} V -> {result}")