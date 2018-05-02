# -*- coding: utf-8 -*-
import os,uuid
import requests
import scrapy
from DouTu.items import DoutuItem
import sys


class DoutuSpider(scrapy.Spider):
    name = "doutu2"
    allowed_domains = ["doutula.com", "sinaimg.cn"]
    start_urls = ['https://www.doutula.com/photo/list/?page={}'.format(i) for i in range(1, 40)]

    def parse(self, response):
        i = 0
        for content in response.xpath('//li[@class="list-group-item"]/div/div/a[@class="col-xs-6 col-sm-3"]'):
            # i += 1
            item = DoutuItem()
            item['img_url'] = content.xpath('.//img/@data-original').extract_first()
            item['name'] = content.xpath('//p/text()').extract_first()
            print(type(item['img_url']))
            print(type(item['name'].encode('utf8')))
            print(item['name'].encode('utf8'))

            try:
                if not os.path.exists('doutu'):
                    os.makedirs('doutu')
                r = requests.get(item['img_url'])
                # filename = 'doutu/%s'%str(uuid.uuid4()) + item['img_url'][-4:]
                filename = 'dt_image/' + item['name'].encode('utf8') + item['img_url'][-4:]
                print('wenjianming',filename)
                with open(filename, 'wb') as fo:
                    fo.write(r.content)
            except Exception as e:
                raise e

            yield item
