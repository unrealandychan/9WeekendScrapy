# -*- coding: utf-8 -*-
import scrapy
from weekend.items import WeekendItem as ITEM


class WeekendFoodSpider(scrapy.Spider):
    name = 'weekend_food'
    start_urls = ['https://www.weekendhk.com/category/dining/page/1/']

    def parse(self, response):
        for links in response.xpath('//div[@class = "article--grid__header"]/a/@href').extract():
            yield scrapy.Request(url = links , callback = self.sub_parse)
        
        nextPage = response.xpath("//div//a[@class='next page-numbers']/@href")[0].extract()

        if nextPage:
            yield scrapy.Request(url= nextPage ,callback = self.parse)

    def sub_parse(self,response):

        # ITEM["date"] = response.xpath('//time/@datetime').extract()
        # ITEM["title"] = response.xpath("//h1/text()").extract()
        # ITEM["content"] = response.xpath('//div[@class = "_content_ AdAsia"]//p/text()').extract()
        # ITEM['link'] = response.url
        # ITEM["tag"] = response.xpath(
        #     "//div[@class = 'btn-list']/a/text()").extract()

        items={
            "Date":response.xpath('//time/@datetime').extract(),
            "Title":response.xpath("//h1/text()").extract(),
            "Author": response.xpath('//div[@class = "_content_ AdAsia"]//p/text()').extract()[0],
            "Content": response.xpath('//div[@class = "_content_ AdAsia"]//p/text()').extract()[1:],
            "Link":response.url,
            "Tag": response.xpath("//div[@class = 'btn-list']/a/text()").extract(),
        }
        yield items
