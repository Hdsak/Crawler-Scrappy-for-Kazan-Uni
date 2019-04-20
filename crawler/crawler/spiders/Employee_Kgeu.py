from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from crawler.items import UniItemLoader, UniItem

import json
url_list=[]
path = "res.json"
with open(path) as json_data:
    d = json.load(json_data)
for k in d:
    for j in k["kaf"]:
        newx=j.replace("Home","Employee")
        newx=newx.replace("Unit","List")
        url_list.append("https://kgeu.ru"+newx)
class Employee(CrawlSpider):
    name = "Employee_Kgeu"
    start_urls = url_list

    def parse(self, response):
        for quote in response.xpath("//div[@class='frame']"):
            yield{
                'kaf_name': quote.xpath("//div[@class='shablon-menu-header']/text()").getall(),
                'employees': quote.xpath("//div[@class='employee-header']//a/text()").getall(),
                'zav_kaf':quote.xpath("//div[class='employee-header']//span/text()")
            }

# Ранжирование по кафедрам иснтитутов и преподавателей
