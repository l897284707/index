class Yichang(Exception):
    def num_Test(self):
        num1=int(input('输入第一条边：'))
        num2=int(input('输入第一条边：'))
        num3=int(input('输入第一条边：'))
        if ((num1+num2>num3)and(num2+num3>num1)and(num1+num3>num2)):
            print('可以组成三角形')
        else :
            raise Yichang(num1)
    su=num_Test(super)