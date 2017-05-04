import requests
from bs4 import BeautifulSoup
from amz_spider_config import headers
import ssl

def get_info_from(detail_page_url):

    web_data = requests.get(detail_page_url, headers=headers, timeout=60)
    soup = BeautifulSoup(web_data.text, 'lxml')

    #通过selector定位到tag上
    asin = soup.select('#averageCustomerReviews')[0]
    review_quantity = soup.select('#acrCustomerReviewText')[0]
    score = soup.select('#acrPopover')[0]

    #存在促销和不促销，价格标签不一样
    if soup.select('#priceblock_saleprice').__len__() == 1:
        price = soup.select('#priceblock_saleprice')[0]
    if soup.select('#priceblock_ourprice').__len__() == 1:
        price = soup.select('#priceblock_ourprice')[0]
    else: price = None  # 没有购物车，没有价格

    buybox_exist = soup.select('#add-to-cart-button')
    feature = soup.select('#feature-bullets > ul > li').__len__() - 1  # 出现6条feature
    print(feature)
    description = soup.select('#productDescription_feature_div')[0].get_text().__len__()

    data = {
        'asin': asin.get('data-asin'),
        'review_quantity': review_quantity.get_text().replace('customer reviews',''),
        'score': score.get_text('', strip=True)[:3],
        'price': price.get_text()[1:] if price!=None else None,
        'buybox_exist': 'Normal' if buybox_exist else 'Abnormal',
        'feature': 'Normal' if feature>=1 and feature<=5 else 'Abnormal',
        'description': 'Normal' if description >100 else 'Abnormal'
    }
    print(data)


if __name__ == '__main__':

    detail_page_url = 'https://www.amazon.com/Enviro-Log-0-65-Fire-Wood-Bundle/dp/B019P4Z740/'
    get_info_from(detail_page_url)