import random
name='玩家'
hero_name =''
ren_win=0
com_win=0
pk_sum=0
def selectHero():
    print('====================欢迎来到19大数据1班游戏对战平台=========================')
    global name
    name =input('请输入您的昵称：')
    hero =input('清选择你要对站的英雄：1.貂蝉 2.白起 3.虞姬 4.伽罗')
    global hero_name
    if hero =='1':
        print('你选择了对战貂蝉')
        hero_name='貂蝉'
    elif hero=='2':
        print('你选择了对战白起')
        hero_name ='白起'
    elif hero=='3':
        print('你选择了对战虞姬')
        hero_name ='虞姬'
    else:
        print('你选择了对战伽罗')
        hero_name ='伽罗'
def ren_com_pk():
    global ren_win
    global com_win
    global pk_sum
    while True:
        pk_sum+=1
        ren_key =int(input('请选择你要出的手势：1.石头 2.剪刀 3.布'))
        if ren_key ==1:
            print('你选择了石头')
        elif ren_key==2:
            print('你选择了剪刀')
        else:
            print('你选择了布')
        com_key = random.randint(1,3)
        if com_key ==1:
            print('电脑选择了石头')
        elif com_key==2:
            print('电脑选择了剪刀')
        else:
            print('电脑选择了布')
        if ren_key ==1 and com_key ==2 or ren_key ==2 and com_key ==3 or ren_key==3 and com_key==1:
            print('你赢了，厉害了我的老baby')
            ren_win +=1
        elif ren_key == com_key:
            print('平局')
        else:
            print('你个小垃圾，输了呢')
        com_win+=1
        if pk_sum >5:
            print('战斗结束了')
            break
def showResult():
    print('========================对站结果的数据显示========================')
    print('%s一共进行了%d局\n你赢了%d局\n电脑赢了%d\n最终显示结果：' % (name,pk_sum,ren_win,com_win))
    if ren_win >com_win:
        print('大吉大利 ，今晚吃X')
    elif ren_win == com_win:
        print('平局，今晚一起XX')
    else:
        print('%s是菜鸡，你不配合我一起XX' % name)
def exits():
    k =input('是否继续？退出按E健，按任意键继续')
    if k =='E':
        print('退出游戏了')
        exit(0)
    else:
        selectHero()
        ren_com_pk()
        showResult()
        exits()
if __name__ =='__main__':
    selectHero()
    ren_com_pk()
    showResult()
    exits()