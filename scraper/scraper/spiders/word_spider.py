import scrapy
import os
import json
import logging
import re

class articleCrawler(scrapy.Spider):
    name = "article"
    #titles = []

    def start_requests(self):
        urls = []
        titles = []

        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "articleLinks.jl"
        abs_file_path = os.path.join(os.path.dirname(os.path.dirname(script_dir)),rel_path)
        with open(abs_file_path) as f:
            add_to_scrape = False
            for line in f:
                tempDict = json.loads(line)
                if (tempDict["Link"] == "doi/full/10.1080/00918369.2012.653313"):
                    add_to_scrape = True
                if(add_to_scrape):
                    urls.append(tempDict["Link"])
                    titles.append(tempDict["Title"])
        for index, url in enumerate(urls):
            yield scrapy.Request(url=("http://www.tandfonline.com"+url),callback=self.parse,dont_filter = True, meta= { 'title' : titles[index], 'index' : index})


    def parse(self,response):
        year =  response.css('div.title-container h2::text').extract_first()

        yield {
            "title" : response.meta['title'],
            'articleText' : response.css('div.abstractSection p::text').extract_first(),
            'date' : re.findall(r'\d+',year )[1],
            'url' : response.url,
            'index' : response.meta['index'],
            }


class linkSpider(scrapy.Spider):
    name = "linky"
    start_urls = ['http://www.tandfonline.com/toc/wjhm20/1/1']

    def parse(self,response):
        next_page = None
        next_issue = None
        for volume in response.css('div.loi-issues-scroller'):
            issues = volume.css('a::attr(href)').extract()
            for issue in issues:
                next_issue = response.urljoin(issue)
                yield {'link' : next_issue }

class WordSpider(scrapy.Spider):
    name = "words"

    def start_requests(self):
        urls = []
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "testLinks.jl"
        abs_file_path = os.path.join(os.path.dirname(os.path.dirname(script_dir)),rel_path)
        with open(abs_file_path) as f:
            for line in f:
                tempDict = json.loads(line)

                urls.append(tempDict["link"])
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        for issue in response.css('div.tocArticleEntry div.art_title'):
            next_page = issue.css('a::attr(href)').extract_first()
            if next_page is not None:
                yield {
                    'Title' : issue.css('span.hlFld-Title::text').extract(),
                    'Link' : issue.css('a::attr(href)').extract_first(),
                }
            else:
                yield {}

    def parseArticles(self,response):
        #logging.warning(response.css('div.abstractSection p::text').extract_first())
        year =  response.css('div.title-container h2::text').extract_first()

        yield {
            'article' : "true",
            'articleText' : response.css('div.abstractSection p::text').extract_first(),
            'date' : re.findall(r'\d+',year )[1],
            'url' : response.url,
            }
'''
            next_page = issue.css('a::attr(href)').extract()
            yield {
                'Title' : issue.css('span.hlFld-Title::text').extract(),
                'Link' : issue.css('a::attr(href)').extract(),
            }

            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parseArticles)

        for issue in response.css('div.tocArticleEntry div.art_title'):
            next_page = issue.css('a::attr(href)').extract()
            yield {
                'Title' : issue.css('span.hlFld-Title::text').extract(),
                'Link' : issue.css('a::attr(href)').extract(),
            }

            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parseArticles)

    def parseArticles(self,response):
'''
