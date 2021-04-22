class Yichang(Exception):
    def num_Test(self):
        PI=3.14
        num = input("输入半径：")
        if num>=0:
            s=PI*(num*num)
            print('半径为%f'%s)
        else :
            raise Yichang(num)
    su=num_Test(super)