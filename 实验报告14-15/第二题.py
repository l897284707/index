class Xuanren(object):
    def juese(self):
        name='null'
        num=int(input('请输入数字：'))
        if num==1:
            name='liubei'
        elif num==2:
            name='zhangfei'
        else :
            name='lvbu'
    def kais(self):
        print('1.石头')
        print('2.剪刀')
        print('3.布')
        num1=int(input('请输入你要选的数：'))
import random
class Diannao(object):
    def ifd(self):
        name='diannao'
    def suiji(self):
        num2=random.random(1,4)
class Guize(Xuanren,Diannao):
    s=Xuanren()
    B=Diannao()
    def ur(self):
        s=Xuanren()
        B=Diannao()
        e=s.kais()
        print(e)
b=Xuanren()
a=Guize()
print(a.ur())