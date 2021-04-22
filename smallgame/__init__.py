import random
list_1=[]
s=0
while s<6:
    w=random.randint(0,3)
    if w==0:
        i=random.randint(0,10)
        list_1.append(str(i))
    elif w==1:
        i=random.randint(65,91)
        list_1.append(chr(i))
    else:
        i=random.randint(97,123)
        list_1.append(chr(i))
    s+=1
for i in list_1:
    print(i,end='')
