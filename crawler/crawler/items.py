import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose


class UniItem(scrapy.Item):
    url=scrapy.Field()
    title=scrapy.Field()
    subtitle=scrapy.Field()
    decription=scrapy.Field()
    kaf=scrapy.Field()

class UniItemLoader(ItemLoader):
    url_out=TakeFirst()
    #url_out=MapCompose(lambda x:x.lower())
    title_out=TakeFirst()
