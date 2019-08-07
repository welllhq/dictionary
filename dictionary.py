import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import re

#作为模块
def dictionary(target):
    #模拟谷歌访问url
    url ='http://www.iciba.com/'
    f_url = url + target
    header = {'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
    req = urllib.request.Request(url = f_url,headers = header)
    reponse = urllib.request.urlopen(req)
    html = reponse.read().decode()#html转码读取

    #使用beautifulsoup 解析html
    soup = BeautifulSoup(html,'lxml')
    res = soup.select('ul>.clearfix>p>span')
    #去标签
    f_res=[]
    for i in res:
        f_res.append(i.text)
    #根据解析内容返回翻译
    return f_res

#若单独运行
if __name__ == '__main__':
   target = input("输入要查询的单词\n")
   print(dictionary(target))

    
