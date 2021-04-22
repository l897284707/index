import os
def file_backups(file_name, path):
    file_back = file_name.split('\\')[-1]
    if os.path.isdir(file_name) is not True:
        with open(file_name, mode='r') as file_data:
            new_path = path + '/' + file_back
            with open(new_path, 'w') as file_back:
                for line_content in file_data.readlines():
                    file_back.write(line_content)
def judge(back_path, file_path):
    if os.path.isdir(file_path) is True:
        file_li = os.listdir(file_path)
        for i in file_li:
            new_file = file_path + '\\' + i
            file_backups(new_file, back_path)
    else:
        if os.path.exists((file_path)):
            file_backups(file_path, back_path)
        else:
            print("备份的文件不存在!")
            exit()
def backups_catalog():
    back_path = input("请输入备份的目录：\n")
    file_path = input("请输入备份的文件:\n")
    if os.path.exists(back_path) is False:
        os.mkdir(back_path)
        judge(back_path, file_path)
        print('备份成功!')
    else:
        judge(back_path, file_path)
        print('备份成功!')
if __name__ == '__main__':
    backups_catalog()