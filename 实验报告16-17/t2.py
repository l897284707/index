with open('ying.txt',mode='r+',encoding='utf-8') as e:
    a=e.read()
    print("修改前文件中的字符：" + a)
    filestr = a.swapcase()
    print("修改后文件中的字符：" + filestr)