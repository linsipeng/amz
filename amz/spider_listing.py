# coding: utf-8

import downloader, database, parser_listing

def crawl(i):

    # 防止任务在一天内被重复执行
    # 多进程下会出错，提前结束！
    # try:
    #     index = database.listing.find().count()-1
    #     if database.listing.find()[index]['date'] == time.strftime('%x'):
    #         print('【Asin基础信息任务】今日已经执行过了！')
    #         return
    # except:
    #     pass

    # 任务开始！
    print('%d条URL待爬取' % database.urls.count())
    print('正在抓取 %s' % i['url'])
    response = downloader.get(i['url'])  # 爬取
    database.urls.remove({'url': i['url']})  # 在url列表里删除这条记录
    parser_listing.parser(response.text)


if __name__ == '__main__':
    a = list(database.urls.find({}))
    crawl(a[0])
