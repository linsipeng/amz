import pymongo
import time
client = pymongo.MongoClient('localhost', 27017)
amz = client['amz']
product_info = amz['product_info']  # 产品页基础信息表。改动频繁，放在config.py里
product_page_url = amz['product_page_url']  # 产品页URL表
keywords = amz['keywords']  # 存放关键词的表
keyword_ranks = amz['keyword_ranks']  # 关键词排名信息表
market_price = amz['market_price']  # 市场价格信息表
contrast = amz['contrast']  # 对比项分析表
listing_health = amz['listing_health']  # Listing健康状况结论表

test = amz['test']
# data = {'asin': 'http://amazon.com'}
# product_page_url.insert(data)
# product_page_url.delete_one(data)

if __name__ == '__main__':
    # product_info.remove({})
    while product_page_url.count()>0:
        time.sleep(2)
        print(product_info.count(),product_page_url.count())
