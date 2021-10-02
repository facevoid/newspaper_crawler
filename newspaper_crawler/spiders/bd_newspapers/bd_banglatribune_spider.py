import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
# newspaper3k
from newspaper import Article

class BDNewspaperCrawler(CrawlSpider):
    name = 'bd_banglatribune_old'
    allowed_domains = ['banglatribune.com']
    start_urls = ['http://www.banglatribune.com/', 'http://www.banglatribune.com/698818/%E0%A7%A7%E0%A7%A7-%E0%A6%98%E0%A6%A3%E0%A7%8D%E0%A6%9F%E0%A6%BE-%E0%A6%AA%E0%A6%B0-%E0%A6%96%E0%A7%81%E0%A6%B2%E0%A6%A8%E0%A6%BE%E0%A6%B0-%E0%A6%B8%E0%A6%99%E0%A7%8D%E0%A6%97%E0%A7%87-%E0%A6%B8%E0%A6%BE%E0%A6%B0%E0%A6%BE%E0%A6%A6%E0%A7%87%E0%A6%B6%E0%A7%87%E0%A6%B0-%E0%A6%9F%E0%A7%8D%E0%A6%B0%E0%A7%87%E0%A6%A8-%E0%A6%9A%E0%A6%B2%E0%A6%BE%E0%A6%9A%E0%A6%B2']

    rules = (
            Rule(LinkExtractor(allow = ('/[0-9]{2,}/')), callback='parse_item', follow=True
                ),
            
            )

    def parse_item(self, response):
        self.logger.info('Hi, this is an item page! %s', response.url)
        print(response.url)
        print('test' * 100)
        url = response.url
        article = Article(url)
        article.download()
        article.parse()
        
        item = scrapy.Item()
        item['url'] = response.url
        item['text'] = article.text
        item['published_date'] = article.publish_date

        return item
