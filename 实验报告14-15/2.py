with open('sd.txt',mode='r+',encoding='utf-8') as e:
    a=e.read()
    e.seek(0,0)
    d=a.index('dee')
    print('dee的坐标是：',d)
    e.seek(2*d,0)
    a=e.write('a大')