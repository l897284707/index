try:
    f = open('123.txt')
except IOError as e:
    print(e)
else:
    data = f.read()
finally:
    f.close()