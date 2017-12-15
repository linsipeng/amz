from bs4 import BeautifulSoup
import lxml, time
import database


def parser(html):

    soup = BeautifulSoup(html, 'lxml')

    # 通过selector定位到tag上
    asin = soup.select('#averageCustomerReviews')[0]
    review_quantity = soup.select('#acrCustomerReviewText')[0]
    score = soup.select('#acrPopover')[0]

    # 存在促销和不促销，价格标签不一样
    if soup.select('#priceblock_saleprice').__len__() == 1:
        price = soup.select('#priceblock_saleprice')[0]
    elif soup.select('#priceblock_ourprice').__len__() == 1:
        price = soup.select('#priceblock_ourprice')[0]
    else:
        price = None  # 没有购物车，没有价格

    # print(price)
    buybox_exist = soup.select('#add-to-cart-button')
    feature = soup.select('#feature-bullets > ul > li').__len__() - 1  # 出现6条feature
    # print(feature) # 有的feature会有6个li
    description = soup.select('#productDescription_feature_div')[0].get_text().__len__()

    data = {
        'date': time.strftime('%x'),
        'asin': asin.get('data-asin'),
        'review_quantity': review_quantity.get_text().replace(' customer review','').replace('s',''),
        'score': score.get_text('', strip=True)[:3],
        'price': price.get_text()[1:] if price != None else price,
        'buybox_exist': 'Normal' if buybox_exist else 'Abnormal',
        'feature': 'Normal' if feature >= 5 else 'Abnormal',
        'description': 'Normal' if description > 100 else 'Abnormal'
    }
    print(data)
    data_filter = {
        'date': time.strftime('%x'),
        'asin': asin.get('data-asin')
    }
    # 防止相同日期的数据被重复采集
    if database.listing.find(data_filter).count() == 0:  # 如果没有重复数据
        database.listing.insert_one(data)  # 那就写入数据库
    else:
        pass

if __name__ == '__main__':
    pass