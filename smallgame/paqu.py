from lxml import html
etree = html.etree
text='''
<div>
<ul>
  <li class="item-1">
    <a href="link1.html">first item</a>
  </li>
  <li class="item-1">
    <a href="link2.html">second item</a>
  </li>
  <li class="item-inactive">
    <a href="link3.html">third item</a>
  </li>
  <li class="item-1">
    <a href="link4.html">fourth item</a>
  </li>
  <li class="item-0">
    <a href="link5.html">fifth item</a>
  </li>
</ul>
</div>'''
html=etree.HTML(text)
li_list=html.xpath("//li[@class='item-1']")
for li in li_list:
    item={}
    item['href']=li.xpath('./a/@href')[0]
    item['title']=li.xpath('./a/text()')[0]
    print(item)