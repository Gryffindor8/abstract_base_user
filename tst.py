from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set the desired port number
port_number = 9222

# Set up the Chrome driver with the specified port
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'--remote-debugging-port={port_number}')

# Start the Chrome driver with the specified port
driver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service, options=chrome_options)

# Perform actions on the browser running on the specified port
driver.get("https://www.example.com")
# ... perform other actions ...
print("ok")
# Close the browser
driver.quit()
