from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Set up WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open Amazon product page
url = "https://www.amazon.in/Boult-Audio-Wireless-Playtime-Bluetooth/dp/B0BQN2RMJF/ref=sr_1_1_sspa?crid=1WN139PWEA9QP&dib=eyJ2IjoiMSJ9.RSgasfsrGRVNex9RWP45TOLZSJ5B-KRXhl8imbMnMWVg68iO3V2FZCu_8gvfXlWA_tQdu4rftSDbbfiKGk6I7iZyVUnk-fXPIv4vrwYyplByukfLV0gZcOzHXaqMEUjZOwJbOPgY2WEFwGQAneW8wCYEJGMCZtOxX8dCArTavqoula8UzoGDjz-e-FMGHHhdewC9NKM1TEPk3hELZTfyE1cxxl2s1_bVCTzYGoPXS5Q.WDkM5Up8guWZNQqGXDcADGY_LGLgajGtPPYd_4WZobU&dib_tag=se&keywords=airpods%2Bpro2&qid=1738740082&sprefix=air%2Caps%2C248&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1"
driver.get(url)

# Wait for the page to load
time.sleep(5)  # Adjust based on internet speed

# Extract product title
try:
    title = driver.find_element(By.ID, "productTitle").text.strip()
except:
    title = "Product name not found"

# Extract price
try:
    price = driver.find_element(By.CLASS_NAME, "a-price-whole").text.strip()
except:
    price = "Price not found"

# Print results
print(f"Product: {title}")
print(f"Price: ₹{price}")

# Close browser
driver.quit()
