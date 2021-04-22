print('''商城目前上架物品：
    可乐：2元
    雪碧：2元
    矿泉水：1元
    面包：2.5元
    烤肠：1元
    钢笔10元
    洗衣粉：5元
    输入END 退出''')
ric={'可乐':'2','雪碧':'2','矿泉水':'1','面包':'2.5','烤肠':'1','钢笔':'10','洗衣粉':'5'}
um=0
while True:
    c=input('请输入需要购买的物品：')
    if c.upper()!='END':
        for i in ric.keys():
            if i ==c :
                s=input('请输入需要购买的数量：')
                sum=0
                sum=float(s)*float(ric[c])
                um+=sum
    else:
        break
print(um)