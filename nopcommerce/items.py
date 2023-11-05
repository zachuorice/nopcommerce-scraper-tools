# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QuickTabItem(scrapy.Item):
    content = scrapy.Field()
    name = scrapy.Field()
    product_slug = scrapy.Field()
    content_url = scrapy.Field()
