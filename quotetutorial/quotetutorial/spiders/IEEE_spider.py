import scrapy
from scrapy.http import FormRequest
from scrapy_splash import SplashRequest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class IEEESpider(scrapy.Spider):
    name = "ieee"
    start_urls = ["https://dl-acm-org.proxy2.library.illinois.edu/conference/comm/proceedings"]

    def parse(self, response, **kwargs):
        driver = webdriver.Chrome('C:\\Users\\Owenz\\Downloads\\chromedriver_win32\\chromedriver.exe',
                                  options=webdriver.ChromeOptions())
        driver.get(self.start_urls[0])

        # Login
        username = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "j_username")))
        password = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "j_password")))

        username.send_keys("")
        password.send_keys("")

        submit = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "_eventId_proceed")))
        submit.click()
        time.sleep(10)
        yield SplashRequest(url=driver.current_url, callback=self.after_login, endpoint='render.html',
                            cookies=driver.get_cookies())

    def after_login(self, response):
        title = response.body
        print("Response:", title)
