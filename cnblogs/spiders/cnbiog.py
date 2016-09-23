#encoding:utf-8
import scrapy
from bs4 import BeautifulSoup
class cnblogsData(scrapy.Spider):
    name = 'cnblogs'
    start_urls = ['http://www.jrj.com.cn/']
    def parse(self, response):
        res = BeautifulSoup(response.body)
        print "这里有没经", res
