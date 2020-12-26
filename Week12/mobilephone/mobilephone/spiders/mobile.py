import scrapy
from scrapy.selector import Selector
from mobilephone.items import MobilephoneItem, MobilephoneCommentItem

class MobileSpider(scrapy.Spider):
    name = 'mobile'
    allowed_domains = ['www.smzdm.com']
    start_urls = ['https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/']


    def parse(self, response):
        print(response.url)

        mobile_phones = Selector(response=response).xpath('//*[@id="feed-main-list"]/li')

        for mobile_phone in mobile_phones[0:10]:

            product_name = mobile_phone.xpath('./div/div[2]/h5/a/text()').extract()[0]
            product_url = mobile_phone.xpath('./div/div[2]/h5/a/@href').extract()[0]
            print(product_name)
            print(product_url)

            yield scrapy.Request(url=product_url,callback=self.parse_comments)


    def parse_comments(self, response):
        
        O_link = response.url
        print(O_link)

        yield scrapy.Request(url=O_link,callback=self.parse_comment,dont_filter=True)

        # print(link)

        # mobiel_phone_name = Selector(response=response).xpath('//*[@id="feed-main"]/div[2]/div/div[1]/h1/text()').extract()[0]
        # mobile_phone_comments = Selector(response=response).xpath('//*[@id="commentTabBlockNew"]/ul[1]/li')

        try:
            mobile_phone_comments_indexs = Selector(response=response).xpath('//*[@id="comment"]/div[1]/ul[2]/li')
            mobile_phone_comments_index = int(mobile_phone_comments_indexs[-4].xpath('./a/text()').extract()[0])
            print(mobile_phone_comments_index)
        except IndexError:
            print('没有翻页')
        else:
            for i in range(2, mobile_phone_comments_index+1):
                T_link = O_link+'p'+str(i)+'/'
                yield scrapy.Request(url=T_link,callback=self.parse_comment)




        # //*[@id="comment"]/div[1]/ul[2]/li[11]/ //*[@id="comment"]/div[1]/ul[2]/li[11]/a //*[@id="comment"]/div[1]/ul[2]/li[8]/a //*[@id="comment"]/div[1]/ul[2]/li[11]/a
        # //*[@id="comment"]/div[1]/ul[2]/li[8]/a
        # print(mobiel_phone_name)

        # for mobile_phone_comment in mobile_phone_comments:
        #     product_name = mobiel_phone_name
        #     user_name = mobile_phone_comment.xpath('./div[2]/div[1]/a/span/text()').extract()[0]
        #     product_comment = mobile_phone_comment.xpath('./div[2]/div[@class="comment_conWrap"]/div[1]/p/span/text()').extract()[0]
        #     #li_comment_179991459 > div.comment_conBox > div.comment_conWrap
        #     print(product_name)
        #     print(user_name)
        #     print(product_comment)

        

    def parse_comment(self, response):

        print(response.url)
        mobiel_phone_name = Selector(response=response).xpath('//*[@id="feed-main"]/div[2]/div/div[1]/h1/text()').extract()[0].strip()
        mobile_phone_comments = Selector(response=response).xpath('//*[@id="commentTabBlockNew"]/ul[1]/li')

        for mobile_phone_comment in mobile_phone_comments:
            product_name = mobiel_phone_name
            user_name = mobile_phone_comment.xpath('./div[2]/div[1]/a/span/text()').extract()[0]
            product_comment = mobile_phone_comment.xpath('./div[2]/div[@class="comment_conWrap"]/div[1]/p/span/text()').extract()[0]
            #li_comment_179991459 > div.comment_conBox > div.comment_conWrap

            comment = MobilephoneCommentItem()
            comment['product_name'] = product_name
            comment['user_name'] = user_name
            comment['product_comment'] = product_comment

            # print(comment)

            # print(product_name)
            # print(user_name)
            # print(product_comment)

            yield comment

        
