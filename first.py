# First.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import sys

# Specify the path to chromedriver if not in PATH
# service = Service('C:/path/to/chromedriver.exe')
# driver = webdriver.Chrome(service=service)

driver = webdriver.Chrome()  # Assumes chromedriver is in PATH
try:
    driver.get('https://www.bbc.com')
    body_text = driver.find_element(By.TAG_NAME, 'body').text
    if 'crime' in body_text.lower():
        print("Test Passed: 'crime' found on BBC website.")
        sys.exit(0)
    else:
        print("Test Failed: 'crime' not found on BBC website.")
        sys.exit(1)
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)
finally:
    driver.quit()
