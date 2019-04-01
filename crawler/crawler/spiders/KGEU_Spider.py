from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from crawler.items import UniItemLoader, UniItem


class KGEU(CrawlSpider):
    name = "KGEU_Spider"
    allowed_domains = [
        'kgeu.ru'
    ]
    start_urls = [
        'https://kgeu.ru/Home/Kafedras/44',
        'https://kgeu.ru/Home/Kafedras/45',
        'https://kgeu.ru/Home/Kafedras/46'
    ]

    rules = (
        Rule(
            LinkExtractor(
                restrict_xpaths=[
                    "//div[@class='white']"
                ],
                # (44|45|46)' #44 45 46 в конце
                allow=r'https://kgeu.ru/Home/Kafedras/\d+$'
            ),

            "parse_item"
        ),
    )

    def parse_item(self, response):
        selector = Selector(response)
        loader = UniItemLoader(UniItem(), selector)
        loader.add_value('url', response.url)
        loader.add_xpath('title', "//div[@class='shablon-menu-header']/text()")
        loader.add_xpath('subtitle', "//div[@class='content-wrapper']//a/text()")
        return loader.load_item()
#Ранжирование по кафедрам иснтитутов и преподавателей