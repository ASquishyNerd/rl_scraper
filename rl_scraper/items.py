# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class trade(scrapy.Item):
    account = scrapy.Field()
    items_has = scrapy.Field()
    items_wants = scrapy.Field()

class item(scrapy.Item):
    name = scrapy.Field()
    color = scrapy.Field()
    amount = scrapy.Field()

class RlScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
