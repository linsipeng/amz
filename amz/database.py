# coding: utf-8

import pymongo, sqlite3

# client = pymongo.MongoClient('localhost', 27017)
# database = client['database']
# urls = database['urls']
# urls_keyword = urls['keyword']
# listing = database['listing']
# rank = database['rank']
# price = database['price']
# report = database['report']
# test = database['test']
# keywords_source = database['keywords_source']
# keywords_down = database['keywords_down']


# sqlite3
conn = sqlite3.connect('sqlite.db')
cu = conn.cursor()
try:
    # cursor游标是马上生效，不需要commit。
    # create table if not exists 可以直接判断是否存在table，不需要try except
    cu.execute("create table if not exists Products(id int(255) primary key, asin char(255), url char(255), review_quantity int(255), score decimal(255,1), price decimal(255,2), buybox_status int(1), bullet_point_status int(1), description_status int(1))")

except sqlite3.OperationalError:
    print('数据库已经被创建！')


if __name__ == '__main__':
    # database.execute("alter table Products add nick_name char(255)")  # 增加字段
    # database.execute("alter table Products add crawed int(1)")  # 增加字段记录是否已爬取
    # database.commit()
    pass
