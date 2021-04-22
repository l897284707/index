import requests
response = requests.get('https://s1.hdslb.com/bfs/static/jinkela/video/asserts/33.png')
with open('D:/Desktop/1.png','wb') as f:
    f.write(response.content)