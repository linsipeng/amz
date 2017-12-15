# coding: utf-8

import base_info
import database


def make_listing_url():
    # 判断是否有残留任务

    for i in base_info.product_base_info:

        print(i['model_name'])
        asin_url = 'https://www.amazon.com//dp/{}/'.format(i['asin'])
        print('生成URL\n', asin_url)

        sql_statement = '''
                INSERT INTO %s (asin, url, crawed)
                VALUES ("%s", "%s", %d);

                    ''' % ("Products", i['asin'], asin_url,0)
        print(sql_statement)
        conn = database.conn
        conn.execute(sql_statement)
        # cn.execute("DELETE FROM Products")
        # exe完SQL语句之后，要commit事务，操作才能生效。
        conn.commit()
        # 关闭了之后就不能再对数据库进行任何操作了。
        # cn.close()
        # cu = database.database.cursor()
        # cu.execute(sql_statement)

        # mongodb.product_page_url.insert_one(data)

def make_keyword_url():

    for i in base_info.product_base_info:
        # print(i)
        for each_keyword in i['keywords']:
            data = {
                'asin': i['asin'],
                'url': 'https://www.amazon.com/',
                'keyword': each_keyword
            }
            print(data)
            database.urls_keyword.insert_one(data)
        # asin_url = 'https://www.amazon.com//dp/{}/'.format(i['asin'])
        # data = {
        #     'url': asin_url
        # }
        # print(data)
        # database.urls.insert_one(data)
        # mongodb.product_page_url.insert_one(data)


if __name__ == '__main__':
    make_listing_url()
    # make_keyword_url()

    pass