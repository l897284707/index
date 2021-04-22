# class Amphibian:
#     name='两栖动物'
#     def features(self):
#         print('幼年用鳃呼吸')
#         print('成年用肺兼皮肤呼吸')
# class Frog(Amphibian):
#     def attr(self):
#         print(f'青蛙是{self.name}')
#         print('我会呱呱叫')
# frog=Frog()
# print(frog.name)
# frog.features()
# frog.attr()
# def digui (ar):
#     if ar==2:
#         return 1
#     else:
#         return ar*sum(ar-1)
# a=digui(20)

def gongbei():
    nu1=int(input())
    nu2=int(input())
    if (nu1>nu2):
        max=nu1
        while True:
            if max%nu1==0 and max%nu2==0:
                print('为%d'%max)
                break
            else:
                max+=1
    elif nu2>nu1:
        max=nu2
        while True:
            if max%nu1==0 and max%nu2==0:
                print('为%d'%max)
                break
            else:
                max+=1
    else:
        return '最小公倍数为%d'%nu1
a=gongbei()