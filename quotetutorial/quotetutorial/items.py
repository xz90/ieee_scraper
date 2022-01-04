# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# Extracted data -> Temporary containers (items) -> Storing in database

import scrapy


class QuotetutorialItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    title = scrapy.Field()
    email = scrapy.Field()
    pass


class IeeeItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    title = scrapy.Field()
    pass
