#-*-coding:utf8-*-
from lxml import etree
html = 'http://s.weibo.com/top/summary?cate=realtimehot'

selector = etree.HTML(html)
print selector

#提取文本
content = selector.xpath('//*[@id="realtimehot"]')
for each in content:
    print each