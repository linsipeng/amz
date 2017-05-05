import requests
from bs4 import BeautifulSoup
import lxml
from config import headers, product_base_info
import mongodb
import ssl, time
url = 'https://www.amazon.com/s/ref=sr_pg_3'


def get_rank_by_html(asin, html):
        '''
        :param html:网页源码html
        :return: 如果找到asin数据，返回int类型的排名数据；否则返回None
        '''
        soup = BeautifulSoup(html, 'lxml') #把源码丢入BeautifulSoup
        lis = soup.select('li[id^=result_]')  # 找到所有以result打头的li
        for i in lis:
            print(i['data-asin'])
            if i['data-asin'] == asin:
                rank = i.get('id')[7:] # result_0
                return int(rank)
        return None


def get_rank_by_keyword(asin, keyword, max_page = 10):
    page = 1
    payload = {'keywords': keyword,
               'page': page
               }

    while page <= 10:
        web_data = requests.get(url, params=payload, headers=headers)
        rank = get_rank_by_html(asin, web_data.text)
        if rank != None:
            return asin, keyword, rank, page  #如果找到商品，返回
        else:
            page += 1
            print('关键词搜索到 %d 页....'%page)
    return asin, keyword, rank, max_page  #如果找不到，返回page=最大值

if __name__ == '__main__':

    rank_data = get_rank_by_keyword('B0171A42S2', 'fan')
    print('Finish!')
    # payload = {'keywords': 'stove fan',
    #            'page': 1
    #            }
    # pass
    # web_data = requests.get(url, params=payload, headers=headers)
    # soup = BeautifulSoup(web_data.text, 'lxml')
    # # li = soup.select('#s-results-list-atf li')
    # lis = soup.select('li[id^=result_]')  # 找到所有以result打头的li
    # for i in lis:
    #     print(i.get('data-asin'))