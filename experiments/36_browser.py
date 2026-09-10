from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://emertxe.com")
    
    title = driver.title
    heading = driver.find_element(By.TAG_NAME, "h1").text
    
    print("Title :", title)
    print("Heading:", heading)

finally:
    driver.quit()