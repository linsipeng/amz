import requests
from bs4 import BeautifulSoup
import lxml
from config import headers, product_base_info
import mongodb
import time


def build_keywords():
    # 通过Asin生成产品页URL
    mongodb.keywords.remove({})  # 先清空
    for i in product_base_info:
        # print(i['model_name'])
        for keyword in i['keywords']:
            data = {
                'asin': i['asin'],
                'keyword': keyword
            }
            print(data)
            mongodb.keywords.insert_one(data)


def get_rank_by_keyword(i, max_page=10):
    # print(keyword)
    asin = i['asin']
    keyword = i['keyword']
    def get_rank_by_html(asin, html, max_page=10):
        '''
        :param html:网页源码html
        :return: 如果找到asin数据，返回int类型的排名数据；否则返回None
        '''
        soup = BeautifulSoup(html, 'lxml')  # 把源码丢入BeautifulSoup
        lis = soup.select('li[id^=result_]')  # 找到所有以result打头的li
        # 移动端
        # lis = soup.select('li[class=sx-table-item] a')  # 数据存在于a标签
        print('本页找到 %d 个商品' % lis.__len__())
        for i in lis:
            # print(i['data-asin'])
            if i['data-asin'] == asin:
                rank = i.get('id')[7:]  # result_0
                return int(rank)
        return None

    url = 'https://www.amazon.com/'
    page = 1
    while page <= 10:
        payload = {
                    'keywords': keyword,
                    'page': page
                }
        page_load = False
        while page_load == False:
            try:
                web_data = requests.get(url, params=payload, headers=headers, timeout=10)
                print(web_data.url)
                page_load = True
            except:  # 发生任何的异常都不管，再来一次
                time.sleep(1)
                print('数据获取失败，1秒后重新连接！')
        print('%s搜索关键词 %s,状态码：%d' % (asin, keyword, web_data.status_code))

        rank = get_rank_by_html(asin, web_data.text)
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
            mongodb.keyword_ranks.insert_one(data)
            # 删除抓取过的keyword
            mongodb.keywords.remove(i)
            return
        else:
            page += 1
            print('关键词搜索到 %d 页....' % page)

    print('商品超出%d页，放弃查找！' % max_page)
    data = {
            'date': time.strftime('%x'),
            'asin': asin,
            'keyword': keyword,
            'rank': rank,
            'page': max_page  #如果找不到，返回page=最大值
            }
    print(data)
    #把排名数据写入数据库
    mongodb.keyword_ranks.insert_one(data)
    # 删除抓取过的keyword
    mongodb.keywords.remove(i)
    return


if __name__ == '__main__':
    # d = {'asin': 'B01MFGEKZO', 'keywords': ['firewood carrier', 'log carrier', 'log tote']}
    # asin = d['asin']
    # keywords = d['keywords']
    # get_rank_by_keywords(asin,*keywords)
    # build_keywords()
    for i in mongodb.keywords.find():
        print(i['asin'], i['keyword'])
        get_rank_by_keyword(i)
    print('Finish!')
