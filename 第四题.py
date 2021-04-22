diyi=dict(M='Monday',W='Wednesday',F='Fridday')
dier=dict(S={'a':'Saturday','u':'Sunday'},T={'u':'Tuesday','h':'Thursday'})
i=input('请输入第一个字母：')
for j in diyi:
    if i == j:
        print(diyi[i])
    else:
        k=input('请输入第二个字母：')
        print(dier[i][k])
        break