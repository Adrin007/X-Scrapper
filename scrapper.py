import os
import ipPicker
import random
import time
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()
def scrapper():
    website = 'https://x.com/i/flow/login'
    X_USERNAME = os.getenv("X_USERNAME")
    X_PASSWORD = os.getenv("X_PASSWORD")
    proxy = ipPicker.pick()
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("--disable-dev-shm-usage") 
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument(f'--proxy-server={proxy}')
    driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()),options=chrome_options)
    try:
        driver.get(website)
        usernameField = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'text')))
        usernameField.send_keys(X_USERNAME)
        buttons = driver.find_elements(By.TAG_NAME,"button")
        buttons[2].click()
        
        passwordField = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.NAME,'password'))
        )
        if passwordField:
            passwordField.send_keys(X_PASSWORD)
            buttons = driver.find_elements(By.XPATH,'//button')
            buttons[3].click()
        else:
            emailField = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.XPATH,'//input[@type="text"]'))
            )
            emailField.send_keys("adrin01062003@gmail.com")
            buttons = driver.find_elements(By.TAG_NAME,"button")
            buttons[2].click()
        
        exploreButton = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable((By.XPATH,"//a[@href='/explore']"))
        )
        exploreButton.click()
        
        trendingButton = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"//a[@href='/explore/tabs/trending']"))
        )
        trendingButton.click()
        
        trendList = WebDriverWait(driver,10).until(
            EC.presence_of_all_elements_located((By.XPATH,"//div[@data-testid='trend']"))
        )
        trends = []
        
        for trend in trendList[0:5]:
            trendTag = trend.find_element(By.XPATH,'./div/div[2]/span')
            trends.append(trendTag.text)
    except Exception as err:
        print(f"Error : {err}")
    finally:
        driver.close()
        print("Session Terminated")
    return trends,proxy

def main():
    scrapper()

if __name__ == "__main__":
    main()