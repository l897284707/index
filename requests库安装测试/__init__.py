import requests
from lxml import html
etree = html.etree
r = requests.get('https://tieba.baidu.com/f?ie=utf-8&kw=%E5%91%A8%E6%9D%B0%E4%BC%A6&red_tag=g2896306195').content.decode('utf-8')
selector=etree.HTML(r)
info = selector.xpath("//div[@class='threadlist_title pull_left j_th_tit ']/a/text()")
for i in info:
    print(i)