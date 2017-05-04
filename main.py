import amz_product_page_spider
from amz_spider_config import product_base_info

for i in product_base_info:
    print(i['model_name'])
    asin_url = 'https://www.amazon.com//dp/{}/'.format(i['asin'])
    print(asin_url)
    amz_product_page_spider.get_info_from(asin_url)