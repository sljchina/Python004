学习笔记

# 反爬虫方案
## 虚拟头部信息
``` python
# pip install fake-useragent
from fake_useragent import UserAgent
ua = UserAgent(verify_ssl=False)

# 模拟不同的浏览器
print(f'Chrome浏览器: {ua.chrome}')
# print(ua.safari)
# print(ua.ie)

# 随机返回头部信息，推荐使用
print(f'随机浏览器: {ua.random}')
```
## cookies 信息伪装
``` python

```

## WebDriver 模拟浏览器行为
``` python
```

## 代理IP


# 数据持久化
## 数据库存储数据

# 分布式爬虫

# 异常的捕获与处理


# 作业思路
## 作业1
### 加入代理：从GitHub找代理

### 修改数据存储过程，增加数据库连接部分功能

### 异常捕获的实现需要再想想

## 作业2
### 模拟登录