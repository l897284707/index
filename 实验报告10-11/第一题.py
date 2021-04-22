def a4(arg):
    ret = {}
    for key,value in arg.items():
        if len(value) > 2:
            ret[key] = value[0:2]
        else:
            ret[key] = value
    return  ret
dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
r = a4(dic)
print(r)