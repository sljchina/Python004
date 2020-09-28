import scrapy
from maoyan.items import MaoyanItem
from scrapy.selector import Selector

class MaoyanSpider(scrapy.Spider):
    name = "maoyan"
    allowed_domains = ['maoyan.com']
    main_url = 'https://maoyan.com'
    
    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)

# //*[@id="app"]/div/div[2]/div[2]/dl/dd[1]/div[2]/a
    def parse(self, response):
        movies = response.xpath('//div[@class="channel-detail movie-item-title"]/a/@href').getall()
        # print(movies)
        # movies_link = []
        main_url = 'https://maoyan.com'
        for i in range(0, 9):
            movie_link = main_url+movies[i]
            print(movie_link)
            yield scrapy.Request(url=movie_link, callback=self.parse2)
        # print(movies_link)
        # yield scrapy.Request(url=movies_link, callback=self.parse2)
    
    def parse2(self, response):
        # movie = Selector(response=response).xpath('//div[@class="channel-detail movie-item-title"]/a/@href')
        # //div[@class="movie-brief-container"]/h1/text()
        # //div[@class="movie-brief-container"]/ul/li/a/text()
        # //div[@class="movie-brief-container"]/ul/li[@class="ellipsis"][3]/text()
        item = MaoyanItem()
        item['name'] = response.xpath('//div[@class="movie-brief-container"]/h1/text()').get()
        item['category'] = response.xpath('//div[@class="movie-brief-container"]/ul/li/a/text()').get()
        item['date'] = response.xpath('//div[@class="movie-brief-container"]/ul/li[@class="ellipsis"][3]/text()').get
        yield item