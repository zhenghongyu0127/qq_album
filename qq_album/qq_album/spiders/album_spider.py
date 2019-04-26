# -*- coding: utf-8 -*-
import scrapy
import json


from qq_album.items import QqAlbumItem


class AlbumSpiderSpider(scrapy.Spider):
    name = "album_spider"

    def start_requests(self):
        start_album_id = input('请输入起始id')
        end_album_id = input('请输入结束id')

        for i in range(int(start_album_id),int(end_album_id)):
            url = 'https://c.y.qq.com/v8/fcg-bin/fcg_v8_album_info_cp.fcg?ct=24&albumid={}&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'.format(i)
            yield scrapy.Request(url,self.album_parse)

    def album_parse(self,response):

        code = json.loads(response.text)['code']
        album_data = json.loads(response.text)['data']
        album_data['code'] = code

        item = QqAlbumItem()
        item['album_data'] = album_data
        return item



    # def parse(self, response):
    #     pass
