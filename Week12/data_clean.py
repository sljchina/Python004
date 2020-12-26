import pandas as pd
from snownlp import SnowNLP
from sqlalchemy import create_engine

# conn_spider = pymysql.connect(host = 'localhost',
#                        port = 3306,
#                        user = 'root',
#                        password = '87886922',
#                        database = 'spider',
#                        charset = 'utf8mb4'
#                         )

# # 获得cursor游标对象
# con1 = conn_spider.cursor()

# # 操作的行数
# count = con1.execute('select * from mobile_commnets')
# print(f'查询到 {count} 条记录')

engine = create_engine('mysql+pymysql://root:87886922@localhost:3306/spider')



# 封装一个情感分析的函数
def _sentiment(text):
    s = SnowNLP(text)
    return s.sentiments

o_data = pd.read_sql_table('mobile_commnets', engine)
o_data.columns = ['id', 'product_name', 'user_name', 'product_comment']
o_data = o_data.dropna()
o_data['score'] = list(map(_sentiment,o_data['product_comment']))


o_data.to_sql('mobile_commnets_score',engine, index=False, if_exists='replace')

# values = [(id,'testuser'+str(id)) for id in range(4, 21) ]
# con1.executemany('INSERT INTO '+ 'mobile_commnets_score' +' values(%s,%s)' ,values)



# con1.close()
# conn_spider.close()

# 执行批量插入
# values = [(id,'testuser'+str(id)) for id in range(4, 21) ]
# cursor.executemany('INSERT INTO '+ TABLE_NAME +' values(%s,%s)' ,values)




