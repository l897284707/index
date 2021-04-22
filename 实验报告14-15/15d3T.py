import random as r
a=r.randint(0,100)
print("计算机产生了一个1~100之间的数")
b=1
while True:
    print("第"+str(b)+"局")
    try:
        d=int(input("请输入你所猜测的数据："))
    except ValueError:
        print("输入内容必须为数字（整数）！")
    else:
        if a==d:
            print("猜对了！")
            break
        elif a<d:
            print("猜大了！")
        else:
            print("猜小了！")
        b+=1
print("游戏结束了！")