raw_items = [
    " ESP32 | 3.31 V | PASS ",
    "STM32 | 3.29 V | PASS",
    "ESP32 | 3.31 V | PASS",
    "PIC16F877A | 5.10 V | FAIL"
]

records = []

for item in raw_items:
    device, value, result = [part.strip() for part in item.split("|")]
    records.append({
    "device": device,
    "value": value,
    "result": result.upper()
 })

unique = []
seen = set()

for record in records:
    key = (record["device"], record["value"], record["result"])
    if key not in seen:
        seen.add(key)
        unique.append(record)

for record in unique:
    print(record)