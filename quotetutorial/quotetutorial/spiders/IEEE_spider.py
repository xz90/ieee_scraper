import scrapy
from scrapy.http import FormRequest
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'ieee'
    start_urls = [
        'https://ieeexplore-ieee-org.proxy2.library.illinois.edu/document/8722413'
    ]

    def parse(self, response, **kwargs):
        token = response.css('')
        return FormRequest.from_response(response,formdata={
            'j_username': 'xz90',
            'j_password': 'Laker4life2021666'
        }, callback=self.start_scraping)

    def start_scraping(self, response):
        title = response.css('title').extract()
        print(title)