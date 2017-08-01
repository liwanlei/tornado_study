# encoding: utf-8
"""
@author: lileilei
@site: 
@software: PyCharm
@file: pachong.py
@time: 2017/8/1 12:56
"""
import  urllib,json
import urllib.request
import sqlite3,random,time
import datetime
import  multiprocessing
def Get_xinwen():
    url='http://www.toutiao.com/api/pc/feed/?min_behot_time=0&category=__all__&utm_source=toutiao&widen=1&tadrequire=true&as=A125B918F0D0A4B&cp=5980E08A348B5E1'
    headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0" }
    response=urllib.request.Request(url,headers=headers)
    html=urllib.request.urlopen(response).read().decode('gbk')
    be=json.loads(html)
    me=be['data']
    for title in me:
        cn = sqlite3.connect('C:\\Users\Administrator\Desktop\\tornado_study\database.db')
        cu = cn.cursor()
        try:
            if len(title['abstract']) !=0:
                if len(title['title'])!=0:
                    cu.execute("INSERT INTO news(title,desc,text,create_time,create_usid,tag_id) VALUES (?,?,?,?,?,?)",
                               (title['title'], title['abstract'][:10], title['abstract'], datetime.datetime.now(), random.randint(1,6), 1))
                    cn.commit()
                cn.close()
        except Exception as e:
            print(e)
            continue
def shehui():
    url = 'http://www.toutiao.com/api/pc/feed/?category=news_society&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A155D9080061933&cp=5980E1F93333DE1'
    headers = {
        "Referer": "http://www.toutiao.com/ch/news_society/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    }
    response = urllib.request.Request(url, headers=headers)
    htm = urllib.request.urlopen(response).read().decode('utf-8')
    html = json.loads(htm)
    me=html['data'][1]
    lo = html['data']
    try:
        for item in lo:
            cn = sqlite3.connect('C:\\Users\Administrator\Desktop\\tornado_study\database.db')
            cu = cn.cursor()
            if len(item['title']) != 0 and len(item['abstract'])!= 0:
                cu.execute("INSERT INTO news(title,desc,text,create_time,create_usid,tag_id) VALUES (?,?,?,?,?,?)",
                           (item['title'], item['abstract'][:10], item['abstract'], datetime.datetime.now(),
                            random.randint(1, 6), 2))
                cn.commit()
            cn.close()
    except:
        pass
def keyji():
    url = 'http://www.toutiao.com/api/pc/feed/?category=news_tech&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1F589386021C90&cp=598011BCD9C07E1'
    headers = {
        "Referer": "http://www.toutiao.com/ch/news_tech/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    }
    response = urllib.request.Request(url, headers=headers)
    htm = urllib.request.urlopen(response).read().decode('utf-8')
    html = json.loads(htm)
    me=html['data'][1]
    lo = html['data']
    try:
        for item in lo:
            cn = sqlite3.connect('C:\\Users\Administrator\Desktop\\tornado_study\database.db')
            cu = cn.cursor()
            if len(item['title']) != 0 and len(item['abstract'])!= 0:
                cu.execute("INSERT INTO news(title,desc,text,create_time,create_usid,tag_id) VALUES (?,?,?,?,?,?)",
                           (item['title'], item['abstract'][:10], item['abstract'], datetime.datetime.now(),
                            random.randint(1, 6), 4))
                cn.commit()
            cn.close()
    except:
        pass
def junshi():
    url = 'http://www.toutiao.com/api/pc/feed/?category=news_military&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A18549284011D7A&cp=5980612D275A0E1'
    headers = {
        "Referer": "http://www.toutiao.com/ch/news_military/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    }
    response = urllib.request.Request(url, headers=headers)
    htm = urllib.request.urlopen(response).read().decode('utf-8')
    html = json.loads(htm)
    me=html['data'][1]
    lo = html['data']
    try:
        for item in lo:
            cn = sqlite3.connect('C:\\Users\Administrator\Desktop\\tornado_study\database.db')
            cu = cn.cursor()
            if len(item['title']) != 0 and len(item['abstract'])!= 0:
                cu.execute("INSERT INTO news(title,desc,text,create_time,create_usid,tag_id) VALUES (?,?,?,?,?,?)",
                           (item['title'], item['abstract'][:10], item['abstract'], datetime.datetime.now(),
                            random.randint(1, 6), 5))
                cn.commit()
            cn.close()
    except:
        pass
def lishi():
    url = 'http://www.toutiao.com/api/pc/feed/?category=news_history&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1B519F89051E4B&cp=5980C14E443B5E1'
    headers = {
        "Referer": "http://www.toutiao.com/ch/news_history/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    }
    response = urllib.request.Request(url, headers=headers)
    htm = urllib.request.urlopen(response).read().decode('utf-8')
    html = json.loads(htm)
    me=html['data'][1]
    lo = html['data']
    for item in lo:
        try:
            cn = sqlite3.connect('C:\\Users\Administrator\Desktop\\tornado_study\database.db')
            cu = cn.cursor()
            if len(item['title']) != 0 or len(item['abstract'])!= 0:
                cu.execute("INSERT INTO news(title,desc,text,create_time,create_usid,tag_id) VALUES (?,?,?,?,?,?)",
                               (item['title'], item['abstract'][:10], item['abstract'], datetime.datetime.now(),
                                random.randint(1,6), 6))
                cn.commit()
            cn.close()
        except:
            continue
def caijing():
    url = 'http://www.toutiao.com/api/pc/feed/?category=news_finance&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A1659988E081ED6&cp=598081FE2DF61E1'
    headers = {
        "Referer": "http://www.toutiao.com/ch/news_finance/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    }
    response = urllib.request.Request(url, headers=headers)
    htm = urllib.request.urlopen(response).read().decode('utf-8')
    html = json.loads(htm)
    me=html['data'][1]
    lo = html['data']
    try:
        for item in lo:
            cn = sqlite3.connect('C:\\Users\Administrator\Desktop\\tornado_study\database.db')
            cu = cn.cursor()
            if len(item['title']) != 0 and len(item['abstract'])!= 0:
                cu.execute("INSERT INTO news(title,desc,text,create_time,create_usid,tag_id) VALUES (?,?,?,?,?,?)",
                           (item['title'], item['abstract'][:10], item['abstract'], datetime.datetime.now(),
                            random.randint(1,6),3))
                cn.commit()
            cn.close()
    except:
        pass
if __name__ =='__main__':
    while 1:
        pool = multiprocessing.Pool(processes=6)
        for item in [Get_xinwen,shehui,keyji,junshi,lishi,caijing]:
            print(item)
            pool.apply_async(item,args=())
        pool.close()
        pool.join()
        time.sleep(100)
