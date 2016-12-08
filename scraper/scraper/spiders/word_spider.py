import scrapy

class WordSpider(scrapy.Spider):
    name = "words"
    start_urls = ['http://www.tandfonline.com/toc/wjhm20/1/1']

    def parse(self,response):
        next_page = None
        for issue in response.css('div.tocArticleEntry div.art_title'):
            
            yield {
                'Title' : issue.css('span.hlFld-Title::text').extract(),
                'Link' : issue.css('a::attr(href)').extract(),
            }
