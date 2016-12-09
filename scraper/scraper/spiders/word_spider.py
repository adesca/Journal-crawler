import scrapy

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
        with open("../../testLinks.jl") as f:
            for line in f:
                tempDict = json.loads(line)
                urls.append(tempDict.link)
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):
        for issue in response.css('div.tocArticleEntry div.art_title'):
            next_page = issue.css('a::attr(href)').extract()
            yield {
                'article' : "True",
                'Title' : issue.css('span.hlFld-Title::text').extract(),
                'Link' : issue.css('a::attr(href)').extract(),
            }

            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield scrapy.Request(next_page, callback=self.parseArticles)

    def parseArticles(self,response):

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
