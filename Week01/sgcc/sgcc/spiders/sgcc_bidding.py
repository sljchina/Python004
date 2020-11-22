import scrapy


class SgccBiddingSpider(scrapy.Spider):
    name = 'sgcc-bidding'
    allowed_domains = ['ecp.sgcc.com.cn/ecp2.0/']
    start_urls = ['https://ecp.sgcc.com.cn/ecp2.0/portal/#/list/list-spe/2018032600289606_1_2018032700291334/']

    def parse(self, response):
        print(response)
