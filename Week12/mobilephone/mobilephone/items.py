# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MobilephoneItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_name = scrapy.Field()
    product_url = scrapy.Field()


class MobilephoneCommentItem(scrapy.Item):
    table = "mobile_commnets"
    product_name = scrapy.Field()
    user_name = scrapy.Field()
    product_comment = scrapy.Field()
    
