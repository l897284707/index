class Yichang(Exception):
    def name_Test(self):
        name = input("输入文件名：")
        suffix = name.split(".")[-1]
        if suffix=='jpg'or suffix=='png' or suffix=='jpeg':
            print(name)
        else :
            raise Yichang(suffix)
    su=name_Test(super)