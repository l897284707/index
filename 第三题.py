dict={'学号':2016001, '姓名':'王浩', 'age':18 ,'住址':'文泽园2#606', '性别':'男'}
print(dict['姓名'])
print(dict['住址'])
dict.update(age=19)
dict.pop('性别')
for k,v in dict.items():
    print('key=%s,valie=%s'%(k,v))
