def addUser(contactlist):
    name = input("请输入姓名:>")
    flag = False
    for index in range(len(contactlist)):
        if (contactlist[index][0] == name):
            print("此联系人已经存在，请重新输入！！")
            flag = True
            break
    if not flag:
        phone = input("请输入手机号:>")
        singlelist = [name, phone]
        contactlist.append(singlelist)
        print("输入完成")
def deleteUser(contactlist):
    name = input("请输入要删除的联系人:>")
    flag = False
    for index in range(len(contactlist)):
        if contactlist[index][0] == name:
            del contactlist[index]
            flag = True
            print("删除成功")
            break
    if not flag:
        print("查无此人！")
def updateUser(contactlist):
    name = input("请输入要修改的联系人:>")
    flag = False
    for index in range(len(contactlist)):
        if contactlist[index][0] == name:
            phone = input("请输入要修改的电话号码:>")
            contactlist[index][1] = phone
            flag = True
            print("修改成功")
            break
    if not flag :
        print("查无此人！")
def getAllUser(contactlist):
    print("-------------------")
    for i in contactlist:
        print("用户：\t%s\t\t%s" % (i[0], i[1]))
    print("-------------------")
def queryPhoneByName(contactlist):
    name = input("请输入要查询的联系人:>")
    flag = False
    for index in range(len(contactlist)):
        if contactlist[index][0] == name:
            print("您要查找的手机号码是：%s" % (contactlist[index][1]))
            flag = True
            break
    if not flag:
        print("查无此人！")
def work(contactlist):
    while True:
        num = input("请根据规则继续输入:>")
        if num not in ['1','2','3','4','5','6']:
            print("输入有误，请重新输入")
        else:
            if num=='1':
                addUser(contactlist)
            elif num == '2':
                deleteUser(contactlist)
            elif num == '3':
                updateUser(contactlist)
            elif num == '4':
                getAllUser(contactlist)
            elif num == '5':
                queryPhoneByName(contactlist)
            elif num == '6':
                print("感谢使用")
                break
def main():
    contactlist = []
    info = '''
    ====通讯录管理系统====
    1.增加姓名和手机
    2.删除姓名
    3.修改手机
    4.查询所有用户
    5.根据姓名查找手机号
    6.退出
    =====================
    '''
    print(info)
    work(contactlist)
if __name__ == "__main__":
    main()