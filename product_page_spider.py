import requests
from bs4 import BeautifulSoup
from config import headers, product_base_info
import mongodb
import ssl, time


def get_info_from(detail_page_url):
    time.sleep(2)  # 2秒间隔，防止速度过快
    web_data = requests.get(detail_page_url, headers=headers, timeout=10)
    soup = BeautifulSoup(web_data.text, 'lxml')

    #通过selector定位到tag上
    asin = soup.select('#averageCustomerReviews')[0]
    review_quantity = soup.select('#acrCustomerReviewText')[0]
    score = soup.select('#acrPopover')[0]

    #存在促销和不促销，价格标签不一样
    if soup.select('#priceblock_saleprice').__len__() == 1:
        price = soup.select('#priceblock_saleprice')[0]
    elif soup.select('#priceblock_ourprice').__len__() == 1:
        price = soup.select('#priceblock_ourprice')[0]
    else: price = None  # 没有购物车，没有价格
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
        'price': price.get_text()[1:] if price!=None else None,
        'buybox_exist': 'Normal' if buybox_exist else 'Abnormal',
        'feature': 'Normal' if feature>=1 and feature<=7 else 'Abnormal',
        'description': 'Normal' if description >100 else 'Abnormal'
    }
    print(data)
    data_filter = {
        'date': time.strftime('%x'),
        'asin': asin.get('data-asin')
    }
    # 防止相同日期的数据被重复采集
    if mongodb.product_info.find(data_filter).count() == 0:  # 如果没有重复数据
        mongodb.product_info.insert_one(data)  # 那就写入数据库
    else:
        pass


def build_product_page_url():
    # 通过Asin生成产品页URL
    mongodb.product_page_url.remove({})  # 先清空
    for i in product_base_info:
        # print(i['model_name'])
        asin_url = 'https://www.amazon.com//dp/{}/'.format(i['asin'])
        data = {
            'model_name': i['model_name'],
            'asin_url': asin_url
        }
        # print(data)
        mongodb.product_page_url.insert_one(data)


if __name__ == '__main__':
    build_product_page_url()