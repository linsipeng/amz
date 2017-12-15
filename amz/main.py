# coding:utf-8

import spider_listing, spider_search_list, spider_price, database, url_builder, base_info
from multiprocessing import Pool


def asin_track():
    # 任务断点续做功能
    if database.urls.count() > 0:
        print('【Asin基础信息任务】>> 上一次任务残留')  # 列表里还有未抓取的连接，一定是上次留下的。
    else:
        url_builder.make_listing_url()

    a = list(database.urls.find({}))
    b = list(database.urls_keyword.find({}))
    pool = Pool()
    pool.map(spider_listing.crawl, a)
    print('finish!')


def rank_track():
    # 任务断点续做功能
    if database.urls_keyword.count() > 0:
        print('【Rank任务】>> 上一次任务残留')  # 列表里还有未抓取的连接，一定是上次留下的。
    else:
        url_builder.make_keyword_url()

    b = list(database.urls_keyword.find({}))
    pool = Pool()
    pool.map(spider_search_list.crawl, b)
    print('【Rank探测】任务完成！')


def price_track():
    map_list = base_info.product_base_info
    pool = Pool()
    pool.map(spider_price.crawl, map_list)
    print('【价格探测】任务完成！')


if __name__ == '__main__':
    asin_track()
    rank_track()
    price_track()
    print('搞掂晒！')
    pass
