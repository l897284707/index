import json
with open('身份证码值对照表.txt',encoding='utf-8') as shenfen:
    shenfen_dict=json.loads(shenfen.read())
    in_num = input('输入前六位：')
    try:
        print(shenfen_dict[in_num])
    except:
        print('输入错误')