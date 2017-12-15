from bs4 import BeautifulSoup
import lxml, time
import database, downloader


def get_price(html):
    '''
    :param html:
    :return:{asin,price}
    '''

    soup = BeautifulSoup(html, 'lxml')

    # 通过selector定位到tag上
    price_list = []
    try:
        price = soup.select('.sx-price-whole')
        for i in price:
            price_list.append(int(i.text))
        return price_list

    except:
        print('价格分析出现错误！')
        quit()


if __name__ == '__main__':
    keyword = 'desiccant packets'.replace(' ','+')
    url = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords='+keyword
    print(url)
    resp = downloader.get(url)
    a = get_price(resp.text)
    print(a)
    avrg_price = sum(a)/a.__len__()
    print('平均价： %d' % avrg_price)
    gold_price = min(a)+(max(a) - min(a))*0.618
    print('黄金分割价：%d' % gold_price)

    print('Finish!')