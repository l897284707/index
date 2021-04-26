from lxml import html
etree = html.etree
parser=etree.HTMLParser(encoding='utf-8')
selector=etree.parse('aaa.html',parser=parser)
info=selector.xpath('//text()')
for i in info:
    print(i)