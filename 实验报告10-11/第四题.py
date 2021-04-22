def xinxi(arg):
    rex={}
    for i in arg.keys():
        if arg[i]=='女':
            rex[i]=arg[i]
    print(rex)
dic={'一杨':'男','聪聪':'女','文':'男'}
r=xinxi(dic)