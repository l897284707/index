def jia(a,b):
    result=a+b
    print('%d+%d=%d'%(a,b,result))
    return
def jian(a,b):
    result=a-b
    print('%d-%d=%d'%(a,b,result))
def cheng(a,b):
    result=a*b
    print('%d*%d=%d'%(a,b,result))
def chu(a,b):
    result=a/b
    print('%d/%d=%d'%(a,b,result))
c=int(input('请输入第一个数：'))
d=int(input('请输入第二个数'))
i=int(input('1.加\n2.减\n3.乘\n4.除\n'))
if i==1:
    jia(c,d)
elif i==2:
    jian(c,d)
elif i==3:
    cheng(c,d)
elif i==4:
    chu(c,d)