import product_page_spider, search_list_spider
import mongodb, time


def get_product_info():
    # product_info

    # 防止任务在一天内被重复执行
    index = mongodb.product_info.find().count()-1
    if mongodb.product_info.find()[index]['date'] == time.strftime('%x'):
        print('【Asin基础信息任务】今日已经执行过了！')
        return

    # 任务断点续做功能
    if mongodb.product_page_url.count() > 0:
        print('【Asin基础信息任务】>> 上一次任务残留')  # 列表里还有未抓取的连接，一定是上次留下的。
    else:
        product_page_spider.build_url_from_asin()

    # 把数据库里的URL抓取完
    while mongodb.product_page_url.count() > 0:
        i = mongodb.product_page_url.find({})[0]  # 取数据库的第一条
        print('>>> URL列表还有 %d 条待抓取......' % mongodb.product_page_url.count())
        try:
            product_page_spider.get_info_from(i['asin_url'])
            mongodb.product_page_url.remove(i)
        except:  # 发生任何的异常都不管，再来一次
            time.sleep(2)
            print('数据获取失败，2秒后重新连接！')
    print('数据抓取完成！')# product_info


def get_market_price():
    # market_price

    pass


def get_keyword_ranks():
    # keyword_ranks

    # 任务断点续做功能
    if mongodb.keywords.count() > 0:
        print('【关键词检测任务】>> 上一次任务残留')  # 列表里还有未抓取的连接，一定是上次留下的。
    else:
        search_list_spider.build_keywords()

    # 把数据库里的URL抓取完
    while mongodb.keywords.count() > 0:

        i = mongodb.keywords.find()[0]
        print(i['asin'], i['keyword'])
        print('>>> 还有 %d 条Asin的排名数据待抓取......' % mongodb.keywords.count())
        search_list_spider.get_rank_by_keyword(i)

    print('排名数据抓取完成！')# product_info


if __name__ == '__main__':
    get_product_info()
    get_keyword_ranks()