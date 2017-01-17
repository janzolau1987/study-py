# -*- coding: utf-8 -*-

import scrapy
from yyh.items import YyhItem

class YyhSpider(scrapy.Spider):
    name = "yaoyaohao.com"
    allowed_domains = ["yaoyaohao.com"]
    start_urls = [
        "http://www.yaoyaohao.com"
    ]

    def parse(self, response):
        for sel in response.xpath('//ul[@class="sort-list"]/li'):
            next_page = sel.xpath('h4/a/@href').extract_first()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parse_search)

    def parse_search(self, response):
        print(response.url)
        # 暂由于ajax采集不了
        # for sel in response.xpath('//ul[@id="searchTableBody"]/li'):
        #     item = YyhItem()
        #     item['goods_id'] = sel.xpath('@id').extract_first()
        #     pinfo = sel.xpath('div[@class="p-desc"]/pinfo/p').extract()
        #     item['goods_name'] = pinfo[0]
        #     item['manufacture'] = pinfo[1]
        #     yield item
