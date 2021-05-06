from lxml import html
etree =html.etree
source = '''
<html>
<head>
    <title>测试</title>
</head>
<body>
    <div class="useful">
        <ul>
            <li class="info">我需要的信息1</li>
            <li class="info">我需要的信息2</li>
            <li class="info">我需要的信息3</li>
        </ul>
    </div>
    <div class="useless">
        <ul>
            <li class="info">我需要的信息1</li>
            <li class="info">我需要的信息2</li>
        </ul>
    </div>
</body>
</html>
'''
selector=etree.HTML(source)
useful=selector.xpath("//div[@class='useful']")
#info_list=useful[0].xpath('ul/li/text()') starswith
info = selector.xpath('//div[@class="useful"]/ul/li/text()')
print(info)
