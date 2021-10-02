# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
#from scrapy import settings
from scrapy.utils.project import get_project_settings

from elasticsearch import Elasticsearch

class NewspaperCrawlerPipeline(object):
    def __init__(self):
        settings = get_project_settings()
        self.es = Elasticsearch(host=settings['ELASTICSEARCH_SERVER'], port = settings['ELASTICSEARCH_PORT'])
    def process_item(self, item, spider):
        self.es.index(index="test-index", body=item)
        return item
