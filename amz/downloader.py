import requests
import time

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Connection': 'keep-alive',
           'Host': 'www.amazon.com',
           'Referer': 'https://www.amazon.com/',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0'
    }

# alibaba数据管家热搜关键词数据
headers2 = {
        'accept-encoding':'gzip, deflate, br',
        'accept-language':'zh-CN,zh;q=0.8',
        'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie':'ali_apache_id=14.127.80.145.1489462176684.963979.2; t=575da9ac5abe9bdf4ee6f63559464b54; acs_usuc_t=acs_rt=ac38c02352fb4ae2a738897cd580c7ae; ali_beacon_id=14.127.81.238.1495071195888.036423.6; v=0; cookie2=1097d154a3911ac29f0df2fac7023c2e; _tb_token_=f13e73e903865; cna=kU5OEe/9FiECAQ5/UJFSkwLv; xman_us_f=x_l=1&x_locale=zh_CN&no_popup_today=n&x_user=CN|Belinda|Zhou|cgs|221867845&last_popup_time=1489462176692; xman_us_t=x_lid=cnchunwang01&sign=y&x_user=Bptjp+iAnykGzRExyYKOQrBA6pWhBTcCNE6JMGJnO7c=&ctoken=17yb5in3jna3u&need_popup=y&l_source=alibaba; intl_locale=zh_CN; intl_common_forever=Pe4LaCzJX0j8n+lwc8J+bxwcVuDuZfOkaaYK+19fpveSEm7Jy8qJsA==; xman_f=kErePS1QKMqyynZdKIj6mgC7n6/UPqmvB0N3f/s7sTkQ/1szW07XYyixcSmEkKfuqeVwWck49Erfc+L3MAZyOHFsQh2RYRl7nzDRUBbwUHxye6GDrdr5M6G71wC1y5khkbAflWOFmDwFSqLtarELeNcrZkgmEfkckWgvbSErof6T7Rls+Z9g+tR79S8iNuxCgCXLSIwAeChGapUrLNScHvVVN6iNX6We5rPOOeEB/eQs0c2RdaENo73YqOMjuylFL7HlpUkuxjSnbA6cr3pv+3h5foriML/ROIOfLJOYPklljjHTJ4jioc+BsTT8z2oPKqOdAZeHBrbCKQN7cZkbfLza/dQprYeiOpufMi3Y0BaFjkfa+mXYk+CggRGxfeBndLtUBVp1MZBO2th1VMjG7A==; ali_ab=14.127.81.238.1495071295571.5; acs_rt=14.127.81.238.1495071196769.0; csg=78a401e1; JSESSIONID=EF6YVEDTO2-5MKKTXCAU1E78KKW9AVV1-MX3VQT2J-SD53; tmp0=eNrz4A12DQ729PeL9%2FV3cfUxiKnOTLFScnUziwxzdQnxN9I19fX2Dolwdgw1dDW38PYOt3QMCzPU9Y0wDgsMMfLSDXYxNVbSSS6xMjSxNDUwNzQ2MjYwNdBJTEYTyK2wMqiNAgCB%2Bhzu; ali_apache_track="mt=3|ms=|mid=cnchunwang01"; ali_apache_tracktmp="W_signed=Y"; xman_t=XtVOvIw5E9SBfCfuV5rjrBUDZRRkCMttiACq43lE9djE6kLDDy5Ukt/NQoK+Gy0dxQ3nVcqFqkZClrnKibmO4YKfZtdSCPuZHW7O53XPi8Ams1EIrDHWTwI4c/N+eqh656sKj3ZTi+C9CN52LfUnoqxll50nfUJ4lJxZJjBkn8lZXsN5CSn3E15T7P/CBT+D/G6vM35IHDlBxtUxzoXPUj22WNpWlbR/36B7ODLGU8p8TUNbnMc0k2tHszqxwxtENeymQAZlBBZh6dHswIKJs3LqOTV9lE9d9gZ7+tHorjwIcIOXzCTlk5f4+7CDeNrlECr27m1JQ3H0cyen1a6Y6pRkqwWOLikIVbzL9rLucBmCUEiPA9Vfcg2NtzbcjUXOMCh1zZppOFJpbehNMXRI1JIbSHfgCkfdJPDd6kJGVQ1beF1o80AWatOzgVTAeZ6fIT46CIsqoyf+SMt+U5LgG909yCYKBFZgl1yVNli/TBeZ7IxbrEpdrMi8DajdG92zGocBOjzufmWUGlu2IW9lrMbR+33e0sqXtvkjdtM8qDn59Mr0lxIz0eV54NAUwFz5wk98QZIooT+zPKyyvNaEySM52epOB+xQdF3ScoAaPTPLKSPtQ7A3/xPahC80PjdUfDjAOCN+5FjeaoAtt+hMTCE3GuyyRR6l8A58wvlmI9J9XL5/SfR+8Q==; l=AmRk3YAPpaNXCy4Uqq55g1iptGhTEohj; isg=Aqmpic1E1MSNqum--r3MQTuYuFWvXK6OZWVF50ubyhDLEs0kmsfPeb1EogHe',
        'origin':'https://hz-mydata.alibaba.com',
        'referer':'https://hz-mydata.alibaba.com/industry/keywords.htm?spm=a2700.7756200.1998618981.71.EeXOT6',
        'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
        'x-requested-with':'XMLHttpRequest'
    }



def get(url, params=None):
    status_code = 0
    while status_code != 200:
        try:
            response = requests.get(url, headers=headers, params=params, timeout=15)
            response.encoding = response.apparent_encoding
            status_code = response.status_code
            print(response.status_code)
        except:
            time.sleep(2)
            print('页面抓取失败，2秒后重试！')
    return response


def post_alibaba(url, data, headers=headers2):
    response = requests.post(url, data=data, headers=headers2)
    print(response.status_code)
    return response


if __name__ == '__main__':
    url = 'https://hz-mydata.alibaba.com/industry/.json?action=CommonAction&iName=searchKeywords&0.975237835236457&ctoken=17yb5in3jna3u&dmtrack_pageid=0e7f51ee0ab14927591cfa5b15c1931e9131901d06'
    keywords = 'stove fan'
    page_size = 30
    page_no = 2
    data = {
        'keywords': keywords,
        'orderBy': 'srh_pv_this_mon',
        'orderModel':'desc',
        'pageSize':page_size,
        'pageNO':page_no
    }
    response = requests.post(url, data=data, headers=headers2)
    print(response.status_code)
    keyword_data = response.json()['value']['data']
    page_quantity = response.json()['value']['total']/page_size  # int类型
    for i in range(1, page_quantity+1):
        print(i)
    for i in keyword_data:
        print(i)