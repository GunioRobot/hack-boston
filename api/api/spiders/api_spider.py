from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from api.items import ApiItem

class apiSpider(CrawlSpider):
    name = "programmableweb.com"
    allowed_domains = ["programmableweb.com"]
    start_urls = ["http://www.programmableweb.com/apis/directory/"]

    rules = (
        Rule(SgmlLinkExtractor(allow=('/api/.*?', )), callback='parse_item'),
    )

    def parse_item(self, response):
        self.log('api %s' % response.url)
        hxs = HtmlXPathSelector(response)
        item = ApiItem()
        item['heading'] = hxs.select('//h1/text()').extract_unquoted()
        item['description'] = hxs.select('//div[2]/div[2]/p/text()').extract_unquoted()
        item['summary'] = hxs.select('//div[4]/dl/dd/text()').extract_unquoted()
        item['category'] = hxs.select('//div[4]/dl[2]/dd/a/text()').extract_unquoted()
        item['tags'] = hxs.select('//div[4]/dl[3]/dd/a/text()').extract_unquoted()
        item['protocol'] = hxs.select('//div[4]/dl[4]/dd/a/text()').extract_unquoted()
        item['format'] = hxs.select('//div[4]/dl[5]/dd/a/text()').extract_unquoted()
        item['homelink'] = hxs.select('//div[4]/dl[6]/dd/a/text()').extract_unquoted()
        return item

