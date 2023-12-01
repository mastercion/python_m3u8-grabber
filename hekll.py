import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os
import time

def process_urls(url_list, channel_list):
    chrome_options = Options()
    chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL", "browser": "ALL"})
    chrome_options.add_argument("--headless")


    for channel_name, url in zip(channel_list, url_list):
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)

        # Logic for button click
        try:
            button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-block.btn-primary.continue-with-ads.mb40"))
            )
            button.click()
            time.sleep(3)  # Wait for 2 seconds after clicking the button
        except Exception as e:
            print(f"Button not found or error occurred on {url}: {e}")

        log_entries = driver.get_log("performance")

        url_found = False
        for entry in log_entries:
            try:
                obj_serialized = entry.get("message")
                obj = json.loads(obj_serialized)
                message = obj.get("message")
                method = message.get("method")

                if method in ['Network.responseReceived', 'Network.requestWillBeSent']:
                    params = message.get("params", {})
                    request = params.get("request", {})
                    found_url = request.get("url", "")
                    
                    if "https://fra" in found_url and '.mp4' not in found_url:
                        print(f"Found URL for {channel_name}: {found_url[:10]}...")
                        update_json_file(channel_name, found_url)
                        url_found = True
                        break

            except Exception as e:
                print(f"Error processing log entry for {channel_name}: {e}")

        if not url_found:
            print(f"No valid URL found for {channel_name}")

        driver.quit()

def update_json_file(channel_name, url):
    json_file_path = os.path.join('programms', f"{channel_name}.json")
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as file:
            data = json.load(file)
        data['channel_url'] = url

        with open(json_file_path, 'w') as file:
            json.dump(data, file, indent=4)
    else:
        print(f"JSON file for {channel_name} not found.")

#channel_list = ["example.com", "QVCStyle.de", "QVC.de", "QVCZwei.de", "hse.de", "hseTrend.de", "hseExtra.de"]
channel_list = ["example.com", "QVC.de", "QVCStyle.de", "QVCZwei.de"]
url_list = ['https://example.com/', 'https://tv.de/live/qvc/', 'https://tv.de/live/qvc-style/', 'https://tv.de/live/qvc-zwei/']

process_urls(url_list, channel_list)
