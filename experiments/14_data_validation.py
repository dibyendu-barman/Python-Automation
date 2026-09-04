records = [
    {"device":"ESP32","test":"Voltage","value":"3.31","result":"PASS"},
    {"device":"ESP32","test":"Current","value":"0.42","result":"PASS"},
    {"device":"","test":"Temperature","value":"52.0","result":"FAIL"},
    {"device":"ESP32","test":"UART","value":"abc","result":"PASS"},
]

errors = []

for number, row in enumerate(records, start=1):
    if not row.get("device"):
        errors.append(f"Row {number}: missing device")
    if row.get("result") not in {"PASS", "FAIL"}:
        errors.append(f"Row {number}: invalid result")
    
    try:
        float(row["value"])
    except (KeyError, ValueError):
        errors.append(f"Row {number}: invalid numeric value")

print("Valid records:", len(records) - len(set(e.split(":")[0] for e in errors)))
print("Errors:")

for error in errors:
    print("-", error)