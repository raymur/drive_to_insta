from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


def instagram_file_upload(username, password, file_path, caption):
    service = Service(executable_path="chromedriver-linux64/chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.get("https://instagram.com")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    username_element = driver.find_element(By.NAME, "username")
    password_element = driver.find_element(By.NAME, "password")
    username_element.clear()
    password_element.clear()
    username_element.send_keys(username)
    password_element.send_keys(password + Keys.ENTER)

    time.sleep(1)
    WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label='New post']"))
    )
    new_post_button = driver.find_element(By.CSS_SELECTOR, "[aria-label='New post']")
    new_post_button.click()

    WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Select from computer')]"))
    ) 
    upload_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Select from computer')]")
    upload_button.click()

    time.sleep(1)
    # File path for linux!! its also hardcoded 
    keyboard = Controller()
    keyboard.type(file_path)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Next')]"))
    ) 
    upload_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Next')]")
    upload_button.click()

    time.sleep(1)
    WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Next')]"))
    ) 
    upload_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Next')]")
    upload_button.click()

    WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Share')]"))
    ) 
    caption_text_area = driver.find_element(By.CSS_SELECTOR, "[aria-label='Write a caption...']")
    caption_text_area.send_keys(caption)
    upload_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Share')]")
    upload_button.click()

    try:
        WebDriverWait(driver, 30).until(
          EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Your post has been shared.')]"))
        )
        print("picture uploaded")
    except TimeoutError:
        print("Error uploading picture")

    driver.quit()
    
    
def test_upload():
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    file_path = "/home/ray/proj/sheets-insta/rrg_run.jpg"
    caption = "caption"
    instagram_file_upload(username, password, file_path, caption)
    
