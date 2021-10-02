import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
# newspaper3k
from newspaper import Article

class BDNewspaperCrawler(CrawlSpider):
    name = 'bd_kalerkantho'
    allowed_domains = ['www.kalerkantho.com']
    start_urls = ['https://www.kalerkantho.com/']

    rules = (
            Rule(LinkExtractor(allow = '/[0-9]{2,4}/'), callback= 'parse_news', follow= True),
            )

    def parse_news(self, response):
        print(response.url)
        url = response.url
        article = Article(url, input_html=response.text)
        article.download()
        article.parse()
        self.log(str(article)) 
        item = {} 
        item['url'] = response.url
        #item['html']= article.html
        item['text'] = article.text
        if len(article.text) < 5:
            raise Exception('Text not parsed')
        item['title'] = article.title
        item['published_date'] = article.publish_date

        yield item
