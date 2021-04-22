from wordcloud import WordCloud
import jieba
new_data='西游记.txt'
f=open(new_data,'r',encoding='utf-8')
t=f.read()
f.close()
ls=jieba.lcut(t)
txt=' '.join(ls)
font=r'C:\Windows\Fonts\msyh.ttc'
wc = WordCloud(font_path=font,background_color='white',
               width=1000,height=800).generate(txt)
wc.to_file('xiyou.jpg')