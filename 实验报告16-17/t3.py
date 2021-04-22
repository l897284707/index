with open('C:/Users/Mr.Li/IdeaProjects/python实验八/实验报告16-17/fenge.txt','r+',encoding='utf-8') as file1:
    girl = []
    boy = []
    count = 1
    for line in file1:
        if line[:6] != '======':
            (name,sline) = line.split(':',1)
            if name == '小甲鱼':
                boy.append(sline)
            if name == '小客服':
                girl.append(sline)
        else:
            boy_name = 'boy_' + str(count) + '.txt'
            girl_name = 'girl_' + str(count) + '.txt'
            boy_file = open(boy_name, 'w')
            girl_file = open(girl_name, 'w')
            boy_file.writelines(boy)
            girl_file.writelines(girl)
            boy_file.close()
            girl_file.close()
            boy = []
            girl = []
            count += 1
boy_name = 'boy_' + str(count) + '.txt'
girl_name = 'girl_' + str(count) + '.txt'
boy_file = open(boy_name, 'w')
girl_file = open(girl_name, 'w')
boy_file.writelines(boy)
girl_file.writelines(girl)
boy_file.close()
girl_file.close()
file1.close()