from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# Function to process each URL and collect logs
def process_url(url, driver, all_logs):
    # Navigate to the website and perform necessary actions
    driver.get(url)

    # Logic for button click, if applicable
    try:
        button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-block.btn-primary.continue-with-ads.mb40"))
        )
        button.click()
    except Exception as e:
        print(f"Button not found or error occurred on {url}: {e}")

    # Wait for the necessary interactions to happen on the page
    # (Consider using WebDriverWait here for specific elements or conditions)

    # Retrieve and append the network logs
    log_entries = driver.get_log("performance")
    for entry in log_entries:
        all_logs.append(entry)

# Main code
if __name__ == "__main__":
    # Define the list of URLs to iterate through
    url_list = ['https://tv.de/live/qvc-zwei/', 'https://tv.de/live/qvc-style/', '...']  # Add your URLs here

    # Set Chrome options for logging
    chrome_options = Options()
    chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})

    # List to store all log entries
    all_logs = []

    # Iterate through each URL
    for url in url_list:
        driver = webdriver.Chrome(options=chrome_options)
        process_url(url, driver, all_logs)
        driver.quit()  # Close the driver after each URL is processed

    # Save all collected log entries to a JSON file
    with open('network_logs.json', 'w') as file:
        json.dump(all_logs, file, indent=4)
