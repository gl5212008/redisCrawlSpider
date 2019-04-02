# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class FilmPipeline(object):
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(host='127.0.0.1', port=27017)
        self.n = 0


    def process_item(self, item, spider):
        self.n += 1
        print('正在录入第（%s）条'%self.n)
        self.client.film.myfilm.insert_one({'name':item['name'],'url':item['url']})
        # self.client.film.myfilm['url'] = item['url']
        return item
