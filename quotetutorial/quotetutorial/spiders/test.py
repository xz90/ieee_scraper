import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'test'
    page_number = 1
    start_urls = [
        'https://quotes.toscrape.com/page/1/'
    ]

    def parse(self, response, **kwargs):
        items = QuotetutorialItem()

        all_div_quotes = response.css('div.quote')

        for quotes in all_div_quotes:
            name = quotes.css('span.text::text').extract()
            title = quotes.css('.author::text').extract()
            email = quotes.css('.tag::text').extract()

            items['name'] = name
            items['title'] = title
            items['email'] = email

            yield items

        next_page = 'https://quotes.toscrape.com/page/'+ str(QuoteSpider.page_number)+'/'

        if QuoteSpider.page_number < 11:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
