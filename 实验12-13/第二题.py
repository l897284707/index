def re(li):
    list2=[]
    for i in range(len(li)):
        f=pow(li[i],2)
        if f >10:
            list2.append(f)
    print(list2)
list1=[1,2,3,4,5]
r=re(list1)