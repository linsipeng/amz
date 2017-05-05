import product_page_spider
from config import product_base_info
import mongodb


product_page_spider.build_url_from_asin()
# 把数据库里的URL抓取完
while mongodb.product_page_url.count() > 0:
    i = mongodb.product_page_url.find({})[0]  # 取数据库的第一条
    print('>>> URL列表还有 %d 条待抓取......' % mongodb.product_page_url.count())
    try:
        product_page_spider.get_info_from(i['asin_url'])
        mongodb.product_page_url.remove(i)
    except:  # 发生任何的异常都不管，再来一次
        print('数据获取失败，重新连接！')

print('数据抓取完成！')