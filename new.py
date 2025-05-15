from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# Optional: For automatic driver management (commented out)
# from webdriver_manager.chrome import ChromeDriverManager

try:
    # Initialize Chrome driver
    service = Service('chromedriver.exe')  # On Windows, use './chromedriver.exe'
    driver = webdriver.Chrome(service=service)

    # Open WhatsApp Web
    driver.get("https://web.whatsapp.com")
    print("WhatsApp Web should now be open in Chrome.")
    input("Scan the QR code, then press Enter to exit...")

except Exception as e:
    print("Something went wrong:", e)
