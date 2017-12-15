import downloader, database, parser_search_list, url_builder
import time


def crawl(i):

    # 任务开始！
    print('%d条ASIN待获取排名信息' % database.urls_keyword.count())
    # print('查找 %s'% i['url'])
    print(i)
    asin = i['asin']
    url = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps'
    keyword = i['keyword']
    page = 1
    max_page = 10
    while page <= max_page:
        payload = {
                    'keywords': keyword,
                    'page': page
                }
        response = downloader.get(url, params=payload)
        print('查找 %s'% response.url, response.status_code)
        rank = parser_search_list.get_rank_by_html(asin, html=response.text)
        if rank is not None:
            print('商品已找到,在第%d页！' % page)
            data = {
                'date': time.strftime('%x'),
                'asin': asin,
                'keyword': keyword,
                'rank': rank,
                'page': page
            }
            print(data)
            # 把排名数据写入数据库
            database.rank.insert_one(data)
            # 删除抓取过的keyword url
            database.urls_keyword.remove(i)
            break  # 跳出while循环
        else:
            page += 1
            print('关键词搜索到 %d 页....' % page)
            if page > 10:
                print('商品超出%d页，放弃查找！' % max_page)
                data = {
                        'date': time.strftime('%x'),
                        'asin': asin,
                        'keyword': keyword,
                        'rank': None,
                        'page': max_page  #如果找不到，返回page=最大值
                        }
                print(data)
                # 把排名数据写入数据库
                database.rank.insert_one(data)
                # 删除抓取过的keyword url
                database.urls_keyword.remove(i)

if __name__ == '__main__':
    b = list(database.urls_keyword.find({}))
    # crawl(b[0])