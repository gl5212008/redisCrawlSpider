# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from film.items import FilmItem
from scrapy_redis.spiders import RedisCrawlSpider


class YgdySpider(RedisCrawlSpider):
    name = 'ygdy'
    # allowed_domains = ['www.ygdy.com']
    # start_urls = ['http://www.ygdy8.net/html/gndy/rihan/list_6_1.html']
    # start_urls = ['http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html']
    redis_key = 'film_url'
    link = LinkExtractor(allow=r'/gndy/rihan/list_6_\d+.html')
    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = FilmItem()
        b_list = response.xpath('//div[@class="co_content8"]/ul//table//tr[2]//td[2]//b')
        for b in b_list:
            name = b.xpath('.//text()').extract()[-2]
            url='http://www.ygdy8.net' + b.xpath('.//a[2]/@href').extract_first()

            item['name'] = name
            item['url'] = url
            # print(name)
            # print(url)
            yield item
