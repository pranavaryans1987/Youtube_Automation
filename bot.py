from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random

proxy_list=[]
#with open('C:\\Users\\prana\\OneDrive\\Desktop\\YT-Bot\\proxy.txt', 'r') as f:
    #proxies=f.readlines()
#print('[***]\tTotal Proxies :',len(proxies))

for j in range(10):
    #URL = "https://www.youtube.com/watch?v=8aqhykKPUFg"
    URL = "https://www.youtube.com/watch?v=EjqTcJNKycA"
    timeToReopenBrowser = 10
    videoLength = 1680
    timeToReopenBrowser = int(timeToReopenBrowser)
    videoLength = int(videoLength)
    all_drivers = []
    for i in range(timeToReopenBrowser):
        service = webdriver.FirefoxService(executable_path="\\home\\kali\\Downloads\\gecckodriver")
        driver = webdriver.Firefox(service=service)
        all_drivers.append(driver)
        driver.get(URL)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='ytp-large-play-button ytp-button']"))).click()
    sleep(videoLength)
    driver.quit()

