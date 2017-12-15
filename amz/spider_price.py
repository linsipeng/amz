import downloader, database, parser_price
import time


def crawl(i):

    # 任务开始！
    url = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps'
    keyword = i['keywords'][0]
    page = 1
    max_page = 2
    while page <= max_page:
        payload = {
                    'keywords': keyword,
                    'page': page
                }
        response = downloader.get(url, params=payload)
        print('查找 %s'% response.url, response.status_code)
        price = parser_price.get_price(response.text)
        for j in price:
            data = {
                'date': time.strftime('%x'),
                'asin': i['asin'],
                'price':j
            }
            database.price.insert_one(data)
            print(data)
        page += 1


if __name__ == '__main__':
    i = {
        'model_name': 'Stove Fan 334',
        'asin': 'B0171A42S2',
        'keywords': ['wood stove fan','ecofan','fireplace fan','heat powered fan','eco fan','stove fan']
    }
    crawl(i)
