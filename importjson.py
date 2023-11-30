from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# Define the list of URLs to iterate through
url_list = ['https://tv.de/live/qvc-zwei/', 'https://another-example-url.com', '...']  # Add your URLs here

# Set Chrome options for logging
chrome_options = Options()
chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})

# Setup WebDriver
driver = webdriver.Chrome(options=chrome_options)

for url in url_list:
    # Navigate to the website and perform necessary actions
    driver.get(url)

    # Add a condition here to wait for and click the button, if applicable for all URLs
    # If the button or its selector changes per URL, you'll need to adjust this part
    try:
        button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-block.btn-primary.continue-with-ads.mb40"))
        )
        button.click()
    except Exception as e:
        print(f"Button not found or error occurred on {url}: {e}")

    # Wait for the necessary interactions to happen on the page
    # (Consider using WebDriverWait here for specific elements or conditions)

    # Retrieve the network logs
    log_entries = driver.get_log("performance")

    # Filter and print entries related to "https://fra"
    for entry in log_entries:
        try:
            obj_serialized = entry.get("message")
            obj = json.loads(obj_serialized)
            message = obj.get("message")
            method = message.get("method")

            # Check for methods related to network requests
            if method in ['Network.responseReceived', 'Network.requestWillBeSent']:
                params = message.get("params", {})
                request = params.get("request", {})
                url = request.get("url", "")
                
                if "https://fra" in url:
                    print(f"URL: {url}")
                    print('--------------------------------------')

        except Exception as e:
            print(f"Error processing log entry: {e}")

# Optional: Close the browser if no longer needed
driver.quit()

