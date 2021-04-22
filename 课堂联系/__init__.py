num1=int(input('输入被除数：'))
num2=int(input('输入除数：'))
assert type(num1)!=int or type(num2)!=int,'请输入整数'
assert num2!=0,'除数不能为0'
result=num1/num2
print(num1,'/',num2,'=',result)