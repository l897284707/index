def t2 (re):
    new1=[]
    l=len(re)
    for i in range(l):
        if (i%2)==1:
            new1=re[i]
    return new1
l1=[1,2,3,'edj']
r=t2(l1)
print(r)