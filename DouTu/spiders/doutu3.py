# -*- coding: utf-8 -*-
import os
import requests
import scrapy
from DouTu.items import DoutuItem


class DoutuSpider(scrapy.Spider):
    name = "doutu3"
    allowed_domains = ["doutula.com", "sinaimg.cn"]
    start_urls = ['https://www.doutula.com/photo/list/?page={}'.format(i) for i in range(1, 50)]

    def parse(self, response):
        for content in response.xpath('//li[@class="list-group-item"]/div/div/a'):
            item = DoutuItem()
            item['img_url'] = content.xpath('.//img/@data-original').extract()[0]
            item['name'] = content.xpath('.//p/text()').extract()[0]

            try:
                if not os.path.exists('doutu'):
                    os.makedirs('doutu')
                r = requests.get(item['img_url'])
                filename = 'dt_image/' + format(item['name']) + item['img_url'][-4:]
                with open(filename, 'wb') as fo:
                    fo.write(r.content)
            except Exception as e:
                raise e

            yield item

