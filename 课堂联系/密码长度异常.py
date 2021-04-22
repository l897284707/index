class ShortInputError(Exception):
    def __init__(self,length,atleast):
        self.length=length
        self.atleast=atleast
try:
    text=input('请输入密码：')
    if len(text)<3:
        raise ShortInputError(len(text),3)
except ShortInputError as result:
    print('ShortInputError：输入的长度是%d，长度至少应是%d'%(result.length,result.atleast))
else:
    print('密码设置成功')