import faker
fa = faker.Faker('zh-cn')
def addUser(contact):
    name = fa.name()
    flag = False  #
    for i in range(len(contact)):
        if contact[i][0] == name:
            print("此联系人已经存在，请重新输入！！")
            flag = True
            break
    if not flag:
        phone = fa.phone_number()
        email = fa.safe_email()
        add = fa.address()
        singles = [name, phone, email, add]
        contact.append(singles)
        print("输入完成")
def deleteUser(contact):
    name = input("请输入要删除的联系人:>")
    flag = False
    for i in range(len(contact)):
        if contact[i][0] == name:
            del contact[i]
            flag = True
            print("删除成功")
            break
    if not flag:
        print("没有该联系人！")
def updateUser(contact):
    name = input("请输入要修改的联系人:>")
    flag = False
    for i in range(len(contact)):
        if contact[i][0] == name:
            phone = input("请输入要修改的电话号码:>")
            contact[i][1] = phone
            email = input("请输入要修改的安全邮箱:>")
            contact[i][2] = email
            add = input("请输入要修改的详细地址:>")
            contact[i][3] = add
            flag = True
            print("修改成功")
            break
    if not flag:
        print("没有该联系人！")
def getAllUser(contact):
    print("-----------------------------------------------------------------------------------------------")
    for i in contact:
        print("姓名：%s\t电话号码：%s\t安全邮箱：%s\t详细地址：%s" % (i[0], i[1], i[2], i[3]))
    print("-----------------------------------------------------------------------------------------------")
def queryPhoneByName(contact):
    name = input("请输入要查询的联系人:>")
    for i in range(len(contact)):
        if contact[i][0] == name:
            print("您要查找的信息是：%s" % (contact[i]))
            flag = True
            if not flag:
                print("没有该联系人！")
def work(contact):
    while True:
        num = input("请继续输入序号进行操作:>")
        if num not in ['1', '2', '3', '4', '5', '6']:
            print("输入有误，请重新输入")
        else:
            if num == '1':
                addUser(contact)
            elif num == '2':
                deleteUser(contact)
            elif num == '3':
                updateUser(contact)
            elif num == '4':
                getAllUser(contact)
            elif num == '5':
                queryPhoneByName(contact)
            elif num == '6':
                # 6.退出
                print("感谢使用寒凡通讯系统")
                break
def main():
    li = []
    info = '''
    ====寒凡通讯录管理系统====
        1.增加联系人
        2.删除联系人
        3.修改手机号码
        4.显示所有联系人
        5.根据姓名查找联系人
        6.退出通讯录系统
    =======================
    '''
    print(info)
    work(li)
if __name__ == "__main__":
    main()