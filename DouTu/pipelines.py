# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import os
import sys
import uuid
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request
from scrapy import log

class DoutuPipeline(object):
    def process_item(self, item, spider):
            try:
                if not os.path.exists('doutu'):
                    os.makedirs('doutu')
            except Exception as e:
                    raise e
            filename = 'doutu/%s'%str(uuid.uuid4()) + item['img_url'][-4:]
            req = requests.get(item['img_url'])
            with open(filename, 'wb') as f:
                f.write(req.content)
            return item


class DouTuImgDownloadPipeline(ImagesPipeline):
    # default_headers = {
    #     'accept': 'image/webp,image/*,*/*;q=0.8',
    #     'accept-encoding': 'gzip, deflate, sdch, br',
    #     'accept-language': 'zh-CN,zh;q=0.8,en;q=0.6',
    #     'cookie': 'bid=yQdC/AzTaCw',
    #     'referer': 'https://www.douban.com/photos/photo/2370443040/',
    #     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    # }

    def get_media_requests(self, item, info):
        yield Request(url = item['img_url'].encode('utf8'))
        # for image_url in item['img_url']:
        #     yield Request(url=image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]  # ok判断是否下载成功
        if not image_paths:
            raise DropItem("Item contains no images")
        # item['image_paths'] = image_paths
        return item