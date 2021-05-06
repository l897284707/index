import requests
from lxml import html
etree = html.etree
secret=requests.get('https://www.baidu.com/').content.decode('utf-8')
selector=etree.HTML(secret)
info=selector.xpath('//*[@id="u1"]/a[1]/text()')[0]
se=selector.xpath('//*[@id="u1"]/a[1]/@href')[0]
print(info)
print(se)