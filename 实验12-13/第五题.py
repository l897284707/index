print('='*18)
print('欢迎使用生词记录本')
print('1.查看单词本')
print('2.背单词')
print('3.添加新单词')
print('4.删除单词')
print('5.清空单词本')
print('6.退出')
print('='*18)
word={}
while True:
    i=int(input('请输入功能编号：'))

    if i == 1:
        print(word.items())
    elif i == 3:
        a=input('请输入新单词：')
        b=input('请输入单词翻译：')
        word[a]=b
        print('单词添加成功！')
        print('单词:'+a+"翻译："+b)
    elif i==6:
        break