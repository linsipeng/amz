from bs4 import BeautifulSoup
import lxml, time
import database


def get_rank_by_html(asin, html):
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
            # print(i['data-asin'], asin)
            if i['data-asin'] == asin:
                rank = i.get('id')[7:]  # result_0
                return int(rank)
        return None


def get_titles_by_html(html):
    soup = BeautifulSoup(html, 'lxml')  # 把源码丢入BeautifulSoup
    h2s = soup.select('li[id^=result_] h2')  # 找到所有以result打头的li,再找到li里面的h2
    print('本页找到 %d 个标题' % h2s.__len__())
    titles = []
    for i in h2s:
        titles.append(i['data-attribute'])
    return titles
    pass


if __name__ == '__main__':
    pass