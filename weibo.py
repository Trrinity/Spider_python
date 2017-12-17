#-*-coding:utf8-*-
from selenium import webdriver
import csv
import codecs
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def writefile(filename,table):
    with open(filename+".csv","w") as file:
        file.write(codecs.BOM_UTF8)
        list = table.split("\n")
        file.write(list[0].replace(" ", ","))
        file.write("\n")
        for i in range(1,len(list)):
            file.write(list[i])

            if i%3==0:
                file.write("\n")
            else:
                file.write(",")
        file.close()

driver =webdriver.Chrome()
driver.get("http://s.weibo.com/top/summary?cate=realtimehot")
table=driver.find_element_by_id("pl_top_realtimehot").text
print(table)

writefile("timehot",table)

