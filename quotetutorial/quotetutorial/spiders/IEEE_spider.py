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

from ..items import QuotetutorialItem


class MySpider(scrapy.Spider):
    name = "lost"
    # allowed_domains = ["mydomain"]
    start_urls = [
        'https://ieeexplore-ieee-org.proxy2.library.illinois.edu/document/8722413',
        "https://shibboleth.illinois.edu/idp/profile/AML2/POST/SSO"
    ]
    myurl = start_urls[0]
    req = 10
    series = {}

    driver = webdriver.Chrome('C:\\Users\\Owenz\\Downloads\\chromedriver_win32\\chromedriver.exe',
                              options=webdriver.ChromeOptions())
    driver.get('https://dl-acm-org.proxy2.library.illinois.edu/conference/comm/proceedings')

    # Login
    username = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "j_username")))
    password = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "j_password")))

    username.send_keys("xz90")
    password.send_keys("Laker4life20216666")

    submit = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, "_eventId_proceed")))
    submit.click()

    # currentUrl = driver.current_url
    # start_urls.insert(0, currentUrl)
    # def start_requests(self):
    #     driver = webdriver.Chrome('C:\\Users\\Owenz\\Downloads\\chromedriver_win32\\chromedriver.exe',
    #                               options=webdriver.ChromeOptions())
    #     driver.get('https://dl-acm-org.proxy2.library.illinois.edu/conference/comm/proceedings')
    #
    #     # Login
    #     username = WebDriverWait(driver, 30).until(
    #         EC.presence_of_element_located((By.ID, "j_username"))
    #     )
    #
    #     password = WebDriverWait(driver, 30).until(
    #         EC.presence_of_element_located((By.ID, "j_password"))
    #     )
    #
    #     username.send_keys("xz90")
    #     password.send_keys("Laker4life20216666")
    #
    #     submit = WebDriverWait(driver, 30).until(
    #         EC.presence_of_element_located((By.NAME, "_eventId_proceed"))
    #     )
    #
    #     submit.click()


        # script = """
        # function main(splash)
        #     local url = splash.args.url
        #     assert(splash: go(url))
        #     assert(splash: wait(30))
        #
        #     splash: set_viewport_full()
        #
        #     local search_input = splash: select('input[name=j_username]')
        #     search_input: send_text("xz90")
        #     assert(splash: wait(30))
        #     local search_input = splash: select('input[name=j_password]')
        #     search_input: send_text("0")
        #     assert(splash: wait(30))
        #     local submit_button = splash: select('input[name=_eventId_proceed]')
        #     submit_button: click()
        #
        #     assert(splash: wait(30))
        #
        #
        #     local submit_button = splash: select('input[name=back]')
        #     submit_button: click()
        #
        #
        #     return {
        #        html = splash: html(),
        #        png = splash: png(),
        #     }
        # end
        # """
        #
        # yield SplashRequest(
        #     self.myurl,
        #     self.parse,
        #     # # #inserting callabck
        #     endpoint='execute',
        #     args={
        #         'lua_source': script,
        #         'ua': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 "
        #               "Safari/537.36 "
        #     },
        # )

    def parse(self, response, **kwargs):
        script = response.body
        print("script: ", script)
        title = response.css('title').extract()
        print("title: ", title)

    def after_login(self, response):
        title = response.css('title').extract()
        print("title: ", title)


class IEEESpider(scrapy.Spider):
    name = 'ieee'
    start_urls = [
        'https://login.proxy2.library.illinois.edu/login?qurl=https://ieeexplore.ieee.org%2fdocument%2f8722413'
    ]

    # TODO:stack overflow one
    # def start_requests(self):
    #     return [
    #         FormRequest(self.start_urls[0], formdata={'j_username': 'xz90',
    #                                                   'j_password': 'Laker4life20216666'}, callback=self.parse)]
    #
    # def parse(self, response, **kwargs):
    #     title = response.css('title').extract()
    #     print(title)

    # TODO:original one
    # def parse(self, response, **kwargs):
    #     token = response.css('form input::attr(value)').extract_first()
    #     return FormRequest.from_response(response, formdata={
    #         'j_username': 'xz90',
    #         'j_password': 'x',
    #         '_eventId_proceed': 'Login',
    #         '_shib_idp_revokeConsent': 'True'
    #     }, callback=self.start_scraping)
    #
    # def start_scraping(self, response):
    #     title = response.css('title').extract()
    #     print(title)

    # TODO:splash test
    # def start_requests(self):
    #     script = """
    #     function main(splash)
    #         local url = splash.args.url
    #         assert(splash:go(url))
    #         assert(splash:wait(10))
    #
    #         splash:set_viewport_full()
    #
    #         local search_input = splash:select('input[name=j_username]')
    #         search_input:send_text("xz90")
    #         local search_input = splash:select('input[name=pj_password]')
    #         search_input:send_text("Laker4life20216666")
    #         assert(splash:wait(5))
    #         local submit_button = splash:select('input[class^=btn btn-primary]')
    #         submit_button:click()
    #
    #         assert(splash:wait(10))
    #
    #         return {
    #             html = splash:html(),
    #             png = splash:png(),
    #         }
    #       end
    #     """
    #     yield SplashRequest(
    #         'https://ieeexplore-ieee-org.proxy2.library.illinois.edu/document/8722413',
    #         callback=self.start_scraping,  ###inserting callabck
    #         endpoint='execute',
    #         args={
    #             'lua_source': script,
    #             'ua': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36"
    #         }
    #     )
    #
    # def parse(self, response, **kwargs):
    #     script = response.body
    #     title = response.css('title').extract()
    #     print(title)
