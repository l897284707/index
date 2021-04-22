import 三方库
with open('data.txt',mode='r+',encoding='gbk') as e:
    a=e.read()
    e.seek(0,0)
    d=a.index('itheima')
    e.seek(d,0)
    a=e.write('黑马')