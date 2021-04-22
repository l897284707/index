old_name=input("请输入要备份的文件名：")
oldfile=open(old_name,'r+',encoding='gbk')
if oldfile:
    num=old_name.rfind('.')
    if num>0:
        fileflag=old_name[num:]
    new_name=old_name[:num]+'[附件]'+old_name[num:]
    new=open(new_name,'w')
    content=oldfile.read()
    new.write(content)
    oldfile.close()
    new.close()