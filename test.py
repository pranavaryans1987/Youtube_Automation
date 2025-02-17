from fp.fp import FreeProxy
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager


class Spoofer(object):

    def __init__(self, country_id=['US'], rand=True, anonym=True):
        self.country_id = country_id
        self.rand = rand
        self.anonym = anonym
        self.userAgent, self.ip = self.get()

    def get(self):
        ua = UserAgent()
        proxy = FreeProxy(country_id=self.country_id, rand=self.rand, anonym=self.anonym).get()

        print(proxy)
        ip = proxy.split("://")[1]
        print(ip)
        return ua.random, ip


def main():
    ser = Service(ChromeDriverManager().install())
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--incognito")
    options.add_argument('--disable-blink-features')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('disable-infobars')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    helperSpoofer = Spoofer()

    webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpsProxy": helperSpoofer.ip,
        "ftpProxy": helperSpoofer.ip,
        "sslProxy": helperSpoofer.ip,
        "proxyType": "MANUAL",
    }

    webdriver.DesiredCapabilities.CHROME['acceptSslCerts'] = True

    options.add_argument("user-agent=" + helperSpoofer.userAgent)

    print(webdriver.DesiredCapabilities.CHROME)

    driver = webdriver.Chrome(options=options, service=ser)

    driver.get("https://www.expressvpn.com/what-is-my-ip")
    time.sleep(25)
    user_agent_check = driver.execute_script(
        "return navigator.userAgent;")
    print(user_agent_check)
    print("done")


if __name__ == "__main__":
    main()