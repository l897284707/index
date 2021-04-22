pingfen=[]
for i in range(10):
    k=int(input('第%d位评委的评分：'%i))
    pingfen.append(k)
pingfen.sort()
sum=0
for l in pingfen[1:9]:
    sum+=l
print(sum/8)