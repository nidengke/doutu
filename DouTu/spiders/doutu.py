# -*- coding: utf-8 -*-
import os
import requests
import scrapy
from scrapy.http import Request
from DouTu.items import DoutuItem


class DoutuSpider(scrapy.Spider):
    name = "doutu"
    allowed_domains = ["doutula.com", "sinaimg.cn"]
    start_urls = ['https://www.doutula.com/photo/list/?page={}'.format(i for i in range(1,3))]

    def parse(self, response):
        a_list = response.xpath('//li[@class="list-group-item"]/div/div/a[@class="col-xs-6 col-sm-3"]')

        for content in a_list:

            item = DoutuItem()
            item['img_url'] = content.xpath('.//img/@data-original').extract_first()
            print(item['img_url'])
            item['name'] = content.xpath('.//p/text()').extract_first()
            print(item['name'])
            # yield Request(url=item['img_url'].encode('utf-8'))
            yield item


    def parse_img(self,response):
        pass
    #     import uuid
    #     try:
    #         if not os.path.exists('doutu'):
    #             os.makedirs('doutu')
    #     except Exception as e:
    #             raise e
    #     filename = 'doutu/%s'%str(uuid.uuid4()) + item['img_url'][-4:]
    #     pass

            # try:
            #     if not os.path.exists('doutu'):
            #         os.makedirs('doutu')
            #     r = requests.get(item['img_url'])
            #     import uuid
            #
            #     # filename = 'doutu/' + str(item['name']) + str(item['img_url'][-4:])
            #     filename = 'doutu/{}'.format(item['name']) + item['img_url'][-4:]
            #     with open(filename, 'wb') as fo:
            #         fo.write(r.content)
            # except Exception as e:
            #     raise e








