import database, base_info
import time, datetime

date = time.strftime('%x')  # str class
today = date
yesterday = datetime.date.today()  - datetime.timedelta(days=1)
yesterday = yesterday.strftime('%x')

def price():

    asin = 'B01ITAZH50'
    price_list = database.price.find({'date':date, 'asin':asin})
    for i in price_list:
        print(i)
    pass

def ranks():

    pass


def show_listing():
    price()
    asin = database.listing.find().sort('asin')
    for i in asin:
        print(i)


def check_normal():
    # 检查buybox、feature、description是否正常
    buybox = database.listing.find({'buybox_exist': 'Abnormal'})
    print(buybox.count())
    feature = database.listing.find({'feature': 'Abnormal'})
    print(feature.count())
    desc = database.listing.find({'description': 'Abnormal'})
    print(desc.count())


def check_review_growth_by_asin(asin):

        try:
            today_quantity = int(database.listing.find({'asin':asin, 'date': today})[0]['review_quantity'])
            yesterday_quantity = database.listing.find({'asin':asin, 'date':yesterday})[0]['review_quantity']
            yesterday_quantity = int(yesterday_quantity)
            if today_quantity > yesterday_quantity:
                print('新增review！')
                print(today_quantity, yesterday_quantity)
            elif today_quantity < yesterday_quantity:
                print('review减少了！')
                print(today_quantity, yesterday_quantity)
            else:
                print('review无增减！')
                print(today_quantity, yesterday_quantity)
        except:
            yesterday_quantity = 0
            print('没有昨天的数据可以对比！')


def check_review_growth():
    print('>'*20+'review增长报告'+'>'*20+'\n')
    for i in base_info.product_base_info:
        asin = i['asin']
        modle_name = i['model_name']
        # asin = 'B0171A42S2'
        check_review_growth_by_asin(asin)
        asin_url = 'https://www.amazon.com//dp/{}/'.format(i['asin'])
        print(modle_name + '\n' + asin_url + '\n'+'-'*50)

if __name__ == '__main__':
    check_review_growth()
    a = input('Finish!')
    pass
