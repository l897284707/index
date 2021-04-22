class heInputError(Exception):
    def __init__(self,length):
        self.length=length
try:
    num=int(input('请输入成绩：'))
    if num<0 or num>150:
        raise heInputError(num)
except heInputError as result:
    print('heInputError：成绩只能在0--150之间'%(result.length))