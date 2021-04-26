import time
import requests
from pprint import pprint
import csv
class TencentSpider(object):
    def __init__(self, start, end):
        self.url = "https://careers.tencent.com/tencentcareer/api/post/Query?&keyword=python&pageIndex={}&pageSize=10"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"
        }
        self.start = start
        self.end = end
    def send_request(self, url):
        """
        发送请求获取响应的方法
        :param url: 要发送请求的url地址
        :return: 返回响应的数据
        """
        response = requests.get(url, headers=self.headers)
        return response.json()
    def save_data(self, data):
        """
        保存数据的方法
        :param data: 要保存的数据
        :return: None
        """
        datas = data["Data"]["Posts"]
        pprint(datas)
        with open('tencent.csv', "w",encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['CategoryName','LastUpdateTime',
                                                   'LocationName','RecruitPostName'])
            writer.writeheader()
            list=[]
            for d in datas:
                dict={'CategoryName':d['CategoryName'],'LastUpdateTime':d['LastUpdateTime'],
                    'LocationName':d['LocationName'],'RecruitPostName':d['RecruitPostName']}
                print(d['RecruitPostName'])
                list.append(dict)
            writer.writerows(list)
        """
        这里已经是获取到数据的一个列表，列表中每个元素是一个字典
        可以根据 字典的key将对应的值取到就可以了
        """
    def run(self):
        for i in range(self.start, self.end + 1):
            time.sleep(3)
            url = self.url.format(i)
            data = self.send_request(url)
            self.save_data(data)
if __name__ == '__main__':
    start = int(input("请输入起始页："))
    end = int(input("请输入终止页："))
    tencent = TencentSpider(start, end)
    tencent.run()
