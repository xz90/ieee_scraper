import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://cs.illinois.edu/about/people/all-faculty'
    ]

    def parse(self, response, **kwargs):

        items = QuotetutorialItem()

        all_professors = response.css('div.item.person.cat15.cs')

        for professor in all_professors:
            name = professor.css('.name a::text').extract()
            title = professor.css('.title::text').extract()
            email = professor.css('.email a::attr(href)').extract()

            items['name'] = name
            items['title'] = title
            items['email'] = email

            yield items


        next_page = response.css('li.next a::attr(href)').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
