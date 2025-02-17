from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


url = "https://www.youtube.com/watch?v=8aqhykKPUFg&ab_channel=PranavTrivedi"
duration = 1090
proxies=[]
with open('proxy.py', 'r') as f:
    proxies=f.readlines()

all_drivers = []
print('[***]\tTotal Proxies :',len(proxies))
for i in range(10):
    proxy = proxies
    options = ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument('--proxy-server=%s' %proxy)
    driver = Chrome(options=options)
    all_drivers.append(driver)
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='ytp-large-play-button ytp-button']"))).click()
sleep(duration)


    