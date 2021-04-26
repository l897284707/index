import requests
r = requests.get('https://item.jd.com/2967929.html')
with open('D:/Desktop/r.text','w') as f:
    r.encoding=r.apparent_encoding#等价于r.content.decode()
    f.write(r.text)