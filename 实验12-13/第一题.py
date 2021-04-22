count=10
def test():
    global count
    count=100
    print(count)
f=test()
print(count)