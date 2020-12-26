# 作业要求
1. ~~正确使用 Scrapy 框架获取评论，如果评论有多页，需实现自动翻页功能。~~
2. ~~评论内容能够正确存储到 MySQL 数据库中，不因表结构不合理出现数据截断情况。~~
3. ~~数据清洗后，再次存储的数据不应出现缺失值。~~
4. Django 能够正确运行，并展示采集到的数据，数据不应该有乱码、缺失等问题。
5. 在 Django 上采用图表方式展示数据分类情况。
6. 舆情分析的结果存入到 MySQL 数据库中。
7. 在 Django 上采用图表方式展示舆情分析的结果。
8. 可以在 Web 界面根据关键字或关键词进行搜索，并能够在页面展示正确的搜索结果。
9. 支持按照时间（录入时间或评论时间）进行搜索，并能够在页面展示正确的搜索结果。
10. ~~符合 PEP8 代码规范，函数、模块之间的调用高内聚低耦合，具有良好的扩展性和可读性。~~

# 开发记录

## 数据抓取与存储
* 创建框架目录
```
scrapy startproject mobilephone
```

* 创建爬虫
```
scrapy genspider mobile www.smzdm.com
```

* 设置数据结构
```
    table = "mobile_commnets"
    product_name = scrapy.Field()
    user_name = scrapy.Field()
    product_comment = scrapy.Field()
```
* 编写数据爬取逻辑

* 用docker创建mysql
```
docker run -p 3306:3306 --name mysql-spider -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag
```
* 创建数据库和数据表

* 设置pipline



## 数据分析并再次存储

* 使用pandas直接读取mysql
```
engine = create_engine('mysql+pymysql://root:87886922@localhost:3306/spider')
o_data = pd.read_sql_table('mobile_commnets', engine)
```
* 使用snownlp分析情感得分
```
def _sentiment(text):
    s = SnowNLP(text)
    return s.sentiments

o_data['score'] = list(map(_sentiment,o_data['product_comment']))

```
* 将含有情感得分的新数据集用pandas写回到mysql中
```
o_data.to_sql('mobile_commnets_score',engine, index=False, if_exists='replace')
```



## 数据展现


