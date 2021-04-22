import requests
def getHTMLText(url):
    try:
        header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 Edg/90.0.818.42'}
        r=requests.get(url,timeout=30,headers=header)
        r.raise_for_status()#如果有异常，不是200，抛出异常
        r.encoding=r.apparent_encoding#等价于r.content.decode()
        return r.text
    except:
        return '产生异常'
if __name__=='__main__':
    url='http://www.baidu.com'
    print(getHTMLText(url))