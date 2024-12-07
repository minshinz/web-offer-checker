from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import os
import threading
import signal

stop_event = threading.Event()
driver = None

def signal_handler(signum, frame):
    global stop_event, driver
    print("\nCtrl+C pressed. Stopping the script...")
    stop_event.set()
    if driver:
        driver.quit()

signal.signal(signal.SIGINT, signal_handler)

def play_sound_repeatedly():
    while not stop_event.is_set():
        os.system('afplay /System/Library/Sounds/Submarine.aiff')
        stop_event.wait(1)  # Wait for 1 second or until stop_event is set

def create_driver(url):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    return driver

def safe_find_and_click(driver, by, value, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()
        return True
    except (TimeoutException, NoSuchElementException):
        return False

def check_string_in_webpage(url, string_to_check, max_attempts=100):
    global stop_event, driver
    for attempt in range(1, max_attempts + 1):
        if stop_event.is_set():
            break
        driver = create_driver(url)
        try:
            # Close popup if it appears
            safe_find_and_click(driver, By.XPATH, "//svg[@data-src='https://icm.aexp-static.com/Internet/Acquisition/US_en/AppContent/OneSite/Data/SVG/dls/dls-icon-close.svg']")
            
            if string_to_check in driver.page_source and string_to_avoid not in driver.page_source:
                print(f"String '{string_to_check}' found in the webpage. Attempt: {attempt}")
                
                # Start playing sound repeatedly
                sound_thread = threading.Thread(target=play_sound_repeatedly)
                sound_thread.daemon = True
                sound_thread.start()
                
                try:
                    button = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Apply Now for The Platinum Card®']"))
                    )
                    button.click()
                    print("Successfully clicked the apply button.")
                    print("Press Ctrl+C to stop the sound and exit...")
                    while not stop_event.is_set():
                        stop_event.wait(1)
                    return True
                except TimeoutException:
                    print("Apply button not found or not clickable. Retrying...")
            else:
                print(f"String '{string_to_check}' not found. Attempt: {attempt}")
            
        except Exception as e:
            print(f"An error occurred: {e}")
        
        finally:
            if driver:
                driver.quit()
                driver = None
        
        if not stop_event.is_set():
            stop_event.wait(3)

    print(f"Max attempts ({max_attempts}) reached or script interrupted.")
    return False

if __name__ == "__main__":
    url = "https://www.americanexpress.com/us/credit-cards/card/platinum/"
    string_to_check = "175,000"
    string_to_avoid = "AS HIGH AS"
    try:
        check_string_in_webpage(url, string_to_check)
    except KeyboardInterrupt:
        pass
    finally:
        stop_event.set()
        if driver:
            driver.quit()
    print("Script terminated.")
