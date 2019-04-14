from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from crawler.items import UniItemLoader, UniItem
import json

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
        loader.add_xpath(
            'subtitle', "//div[@class='content-wrapper']//a/text()")
        loader.add_xpath('kaf',"//div[@class='content-wrapper']//a/@href")
        return loader.load_item()
# Ранжирование по кафедрам иснтитутов и преподавателей


# def parse(self, response):
#     for quote in response.css("div.quote"):
#         yield{
#             'text': quote.css("span.text::text").get(),
#             'author': quote.css("small.author::text").get(),
#             'tags': quote.css("div.tags a.tag::text").getall(),
#         }
#     next_page = response.css("li.next a::attr(href)").getall()
#     if next_page is not None:
#         yield response.follow(next_page, callback=self.parse)
