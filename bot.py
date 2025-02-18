from selenium import webdriver
from urllib.request import urlopen
import re as r
from selenium.webdriver.common.proxy import Proxy, ProxyType
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

for j in range(10):
    #URL = "https://www.youtube.com/watch?v=8aqhykKPUFg"
    URL = "https://www.youtube.com/watch?v=EjqTcJNKycA"
    timeToReopenBrowser = 2
    videoLength = 1680
    timeToReopenBrowser = int(timeToReopenBrowser)
    videoLength = int(videoLength)
    all_drivers = []
    for i in range(timeToReopenBrowser):
        options = webdriver.FirefoxOptions()
        options.set_preference("network.proxy.type", 1)
        options.set_preference("network.proxy.socks", "127.0.0.1")
        options.set_preference("network.proxy.socks_port", 9050)
        options.set_preference("network.proxy.socks_version", 5)
        service = webdriver.FirefoxService(executable_path="/usr/local/bin/geckodriver")
        driver = webdriver.Firefox(service=service,options=options)
        all_drivers.append(driver)
        driver.get(URL)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='ytp-large-play-button ytp-button']"))).click()
        def getIP():
            d = str(urlopen('http://checkip.dyndns.com/').read())
            return r.compile(r'Address: (\d+\.\d+\.\d+\.\d+)').search(d).group(1)
        print(getIP())
    sleep(videoLength)
    driver.quit()
