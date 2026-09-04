import platform
import sys
print("=== System Information ===")
print("OS:", platform.system())
print("OS Version:", platform.version())
print("Machine:", platform.machine())
print("Python:", sys.version.split()[0])