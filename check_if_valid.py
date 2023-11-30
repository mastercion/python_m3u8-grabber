from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#def check_stream_url(stream_url):
#    # Skip URLs containing '.mp4'
#    if '.mp4' in stream_url:
#        print(f"Invalid URL (contains .mp4): {stream_url}")
#        return
#
#    # Setup WebDriver for checking the stream URL
#    driver_check = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#    driver_check.get("https://players.akamai.com/players/dashjs")
#
#    # Find the input field and enter the stream URL
#    input_field = WebDriverWait(driver_check, 20).until(
#        EC.presence_of_element_located((By.ID, "selectedstream"))
#    )
#    input_field.send_keys(stream_url)
#
#    # Find and click the 'Play stream' button
#    play_button = WebDriverWait(driver_check, 20).until(
#        EC.element_to_be_clickable((By.ID, "playButton"))
#    )
#    play_button.click()
#
#    # Wait for 10 seconds
#    time.sleep(10)
#
#    # Check for the presence of "No bitrates found" text
#    bitrates_text = driver_check.find_element(By.CSS_SELECTOR, "td.m-0.p-0").text
#    if "No bitrates found" in bitrates_text:
#        print(f"{stream_url}: No bitrates found")
#    else:
#        print(f"{stream_url}: Bitrates available")
#
#    # Close the browser for check_stream_url
#    driver_check.quit()