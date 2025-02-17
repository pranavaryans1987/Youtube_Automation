import concurrent.futures
import sys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.common.by import By

url = "https://www.youtube.com/watch?v=8aqhykKPUFg&ab_channel=PranavTrivedi"
duration = 1090
proxies=[]
try:
    with open('proxy.py', 'r') as f:
        proxies=f.readlines()
except:
    print('[ERROR]\t"proxy-list.txt" file NOT FOUND !!')
    exit()
print('[***]\tTotal Proxies :',len(proxies))

def getViews(proxy):
    options = ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument('--proxy-server=%s' %proxy)
    #options.add_argument('--window-size=640,480')

    try:
        driver = Chrome(options=options)
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='ytp-large-play-button ytp-button']"))).click()
    except:
        pass
    driver.quit()

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(getViews, proxies)