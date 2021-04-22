def hanshu1(q):
    i=0
    while True:
        i+=1
        if q!=1:
            if q%2==0:
                q=q/2
            elif q%2==1:
                q=3*q+1
        else:
            print(i-1)
            break

e=int(input('请输入数字：'))
r=hanshu1(e)