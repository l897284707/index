import jieba
with open('西游记.txt','r',encoding='utf8') as f:
    str = f.read()
ret = jieba.lcut(str)
dic = {}
for word in ret:
    if len(word) == 1:
        continue
    dic[word] = dic.get(word, 0) + 1
    excluedes = ["行者","大圣","呆子","小妖",'猴子','我们','那里',
                 '一个','怎么','不知','两个','什么','师父','三藏','不是']
dic['孙悟空'] = dic['行者'] + dic['猴子'] + dic['大圣']
dic['唐僧'] = dic['师父'] + dic['三藏']+dic['和尚']
dic['妖精'] = dic['小妖']
for i in excluedes:
    del dic[i]
lis = list(dic.items())
lis.sort(key=lambda x:x[1],reverse=True)
for i in range(8):
    print(lis[i][0])