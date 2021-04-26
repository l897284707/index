import requests
def getHTMLText(url):
    keyword='keyword'
    try:
        header={'q':keyword}
        r=requests.get(url,timeout=30,params=header)
        r.raise_for_status()#如果有异常，不是200，抛出异常
        r.encoding=r.apparent_encoding#等价于r.content.decode()
        return len(r.text)
    except:
        return '产生异常'
if __name__=='__main__':
    url='http://www.so.com/s?'
    print(getHTMLText(url))