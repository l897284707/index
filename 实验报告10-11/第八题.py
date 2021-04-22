def hanshu(rt):
    new_list=[]
    for idx in range(rt):
        if idx == 0:
            new_list.append(1)
        elif idx==1:
            new_list.append(1)
        else:
            new_list.append(new_list[idx - 2] + new_list[idx - 1])
    print(new_list)
rt=int(input('请输入数列循环次数：'))
r=hanshu(rt)