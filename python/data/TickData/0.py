# -*- coding: UTF-8 -*-
# 导入相关包及函数
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates 
import datetime 
# 取得成交信息
I020 = [ line.strip('\n').split(",") for line in open('Futures_20170815_I020.csv')][1:] 
# 将时间字符串转换至时间格式
Time = [ datetime.datetime.strptime(line[0],"%H%M%S%f") for line in I020 ] 
# 通过mdates.date2num函数将datetime时间格式转换为绘图专用的时间格式
Time1 = [ mdates.date2num(line) for line in Time ]
# 价格由字符串转为数值
Price = [ int(line[4]) for line in I020 ]
# 定义图表对象
ax = plt.figure(1)    #第一张图片 
ax = plt.subplot(111) #该张图片仅一个图案
# 以上两行可简写为如下一行
# fig,ax = plt.subplots()
# 绘制图案
# plot_date(x轴对象, y轴对象, 线风格)
ax.plot_date(Time1, Price, 'k-')
# 定义title
plt.title('Price Line')
# 定义x轴
hfmt = mdates.DateFormatter('%H:%M:%S')
ax.xaxis.set_major_formatter(hfmt)
# 显示绘制图表
plt.show()