string='神医一杨'
with open('sd.txt',mode='w',encoding='utf-8') as f:
    size=f.write(string)
    print(size)