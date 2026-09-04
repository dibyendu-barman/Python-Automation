import logging
from pathlib import Path

Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    filename="logs/automation.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logging.info("Automation started")
voltage = 3.31

if 3.20 <= voltage <= 3.40:
    logging.info("Voltage test PASS")
else:
    logging.error("Voltage test FAIL")
    
logging.info("Automation completed")
print("Execution complete. Check logs/automation.log")