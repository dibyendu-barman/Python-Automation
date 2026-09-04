measurements = [3.31, 3.28, 3.35, 3.22, 3.41, 3.30, 3.80]

minimum = min(measurements)
maximum = max(measurements)
average = sum(measurements) / len(measurements)

valid = [v for v in measurements if 3.20 <= v <= 3.40]

print("Measurements:", measurements)
print(f"Minimum : {minimum:.2f} V")
print(f"Maximum : {maximum:.2f} V")
print(f"Average : {average:.2f} V")
print("Valid :", len(valid), "/", len(measurements))