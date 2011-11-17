# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ApiItem(Item):
    # define the fields for your item here like:
    heading = Field()
    description = Field()
    summary = Field()
    category = Field()
    tags = Field()
    protocol = Field()
    format = Field()
    homelink = Field()
    pass
