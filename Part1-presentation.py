# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 22:10:58 2018

@author: Administrator
"""

# %% 给大家看一个小例子

# print('\n'.join([''.join([('Love'[(x-y)%4]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))
#
# # %% 我的第一个Python程序, 在spyder中大家可以用“#%%”进行分块。
# """
# 这是一个
# 多行注释
# """
# print('Hello World!')       # 第一个程序
#
# # %% 基本数据类型
#
# # Number 数据类型
# print('\n****** Number数据类型 ****** ')
# a = 5
# b = 2.0
# print('a的值是:', a)
# print('a的数据类型是：', type(a))
# print('b的值是:', b)
# print('b的数据类型是：', type(b))
# print('a + b = ', a + b)
# print('a / b = ', a / b)        # 结果是浮点型
#
# c = True
# print('c的值是:', c)
# print('c的数据类型是：', type(c))
#
# d = 1 - 2j
# print('d的值是:', d)
# print('d的数据类型是：', type(d))
#
# # String 数据类型
# print('\n****** String数据类型 ****** ')
# str1 = 'Hello everyone!'
# print('str1 = ', str1)
# print('str1[2:7] = ', str1[2:7])
# print('str1[2:] = ', str1[2:])
# print('str1[-1] = ', str1[-1])
# print('str1 + str1 = ', str1 + str1)
#
# # List 数据类型
# print('\n****** List数据类型 ****** ')
# list1 = [1, 5, 3, 7, 9]
# print('list1 = ', list1)
# print('list1[2:4] = ', list1[2:4])
# print('list1[2:] = ', list1[2:])
# print('list1[-1] = ', list1[-1])
# print('list1 + list1 = ', list1 + list1)
# list1.append(11)
# print('list1.append(11) 以后的效果是这样的：')
# print('list1 = ', list1)
# list1.pop()
# print('list1.pop() 以后的效果是这样的：')
# print('list1 = ', list1)
# list1.sort()
# print('list1.sort() 以后的效果是这样的：')
# print('list1 = ', list1)
# list1[0] = 3
# print('list1[0] = 3 以后的效果是这样的：')
# print('list1 = ', list1)
#
# # Tuple 数据类型
# print('\n****** Tuple数据类型 ****** ')
# tuple1 = (2, 4, 6, 8, 10)
# print('tuple1 = ', tuple1)
# print('tuple1[2:4] = ', tuple1[2:4])
# print('tuple1[2:] = ', tuple1[2:])
# print('tuple1[-1] = ', tuple1[-1])
# print('tuple1 + tuple1 = ', tuple1 + tuple1)
# print('与list不同的是，tuple不能更改其中的元素。')
#
# # Set数据类型
# print('\n****** Set数据类型 ****** ')
# set1 = {'张三', '李四', '王五'}
# print('set1 = ', set1)
# print('Set数据类型常常被用来做去重。')
# print('去重以前，list1 = ', list1)
# print('去重以后，list2 = ', list(set(list1)))
#
# # Dictionary数据类型
# print('\n****** Dictionary数据类型 ****** ')
# dict1 = {'Tom': 23, 'Marry': 26, 'Bob': 24}
# print('dict1 = ', dict1)
# print('dict1.keys() = ', dict1.keys())
# print('dict1.values() = ', dict1.values())
# print('索引：dict1["Marry"] = ', dict1["Marry"])
# print('添加一条记录：dict["Lily"] = 23')
# dict1['Lily'] = 23
# print('dict1 = ', dict1)
#
# # 这一部分内容可以在该网址中查看详情：http://www.runoob.com/python3/python3-data-type.html
#
# #%% 选择语句的案例
# age = input('请输入相亲对象的年龄：')   # 例如来了一个相亲对象的年龄是24岁。
# age = int(age)
# print('相亲对象{}岁了'.format(age))
# if age > 32:
#     print('年龄太大，不见。')
# elif age < 18:
#     print('年龄太小，不见。')
# else:
#     print('见。')
#
# #%% 循环的案例
# import time             # 导入时间系统包
# counter = 0             # 初始化计数器
# while counter < 10:     # 当counter满足条件时执行
#     counter += 1
#     print('第' , int(counter) , '个俯卧撑。。。')
#     time.sleep(1)     # 延迟0.5秒
# print('做完了。')
#
# # %% 循环嵌套选择案例1
#
# a = -2
# for i in range(5):
#     print('\n当前a的值是：', a)
#     if a > 0:
#         print('a是一个正数')
#     elif a == 0:
#         print('a是零')
#     else:
#         print('a是一个负数')
#     a = a + 1
#
# #%% 循环嵌套选择案例2
#
# from tqdm import tqdm        #进度条库
# import random
# lifetime = 80 + random.randint(10, 30) # 80 ~ 110的随机整数
# print('我的梦想')
# for age in tqdm(range(lifetime)):
#     time.sleep(0.2)
#     if age == 18:
#         print('\n%s岁：考个好学校；' % age)
#     elif age == 24:
#         print('\n%s岁：找个好工作；' % age)
#     elif age == 27:
#         print('\n%s岁：找个好对象；' % age)
#     elif age == 30:
#         print('\n%s岁：生个好孩子；' % age)
#     elif age == 40:
#         print('\n%s岁：养家糊口ing；' % age)
#     elif age == 50:
#         print('\n%s岁：家庭和睦，事业有成；' % age)
#     elif age == 60:
#         print('\n%s岁：到处旅游；' % age)
#     elif age == 70:
#         print('\n%s岁：锻炼身体；' % age)
#     elif age == 90:
#         print('\n%s岁：子孙满堂。' % age)
        
# %% 爬取新闻vesion1
# coding=utf-8
import requests  #导入HTTP库
from bs4 import BeautifulSoup #导入网页解析库

url_news = "https://www.csdn.net/"
# 获取html文档,以文本形式获取网页源码
response = requests.get(url_news).text  
#用lxml解析器解析网页              
soup = BeautifulSoup(response, 'html.parser')   
# 通过select获取属性content,通过len获取列表长度  
news_list =[]      
for i in range(len(soup.select("h3[class='company_name'] a"))):   
    #通过get_text()获取文本内容
    news_content = soup.select("h3[class='company_name'] a")[i].get_text().strip('\n')
    print(str(i) + '\n' + news_content)
    news_list.append(news_content)
        
# %%爬取新闻version2                 
        
# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# html = urlopen("https://www.csdn.net/").read().decode('utf-8')
# soup = BeautifulSoup(html,"html.parser")
# titles=soup.select("h3[class='company_name'] a") # CSS 选择器
# for title in titles:
#     print(title.get_text(),title.get('href'))# 标签体、标签属性
