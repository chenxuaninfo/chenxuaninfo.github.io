import pymysql.cursors
import pandas  as pd
import matplotlib.pyplot as plt

#######################################################
db=pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='root',db='employees',charset='utf8')
cursor=db.cursor()
#######################################################
try:
	cursor.execute("""
	select * from 
	(WITH tx as (
	SELECT
		DISTINCT(ROUND(salaries.salary/10000,0)) as salary,
		count( salaries.salary ) AS num 
	FROM
		salaries 
	GROUP BY
		salaries.salary
	)
	SELECT
		DISTINCT(CONCAT(salary*10000,'rmb')) as x,
		PERCENT_RANK() OVER (ORDER BY salary desc) AS y,
		sum(num) as z
	FROM
		tx
	GROUP BY salary*10000) as a
	where a.y>0.8
	""")
	res=cursor.fetchall()
	df=pd.DataFrame( [[j for j in i] for i in res] )
	print(df.head())
	x = df[0]
	y = df[1]
	z = df[2]
except:
   print ("Error: unable to fetch data")
# 关闭数据库连接
db.close()
#######################################################
# 饼图
plt.pie(y, labels=x, autopct='%.2f%%')
plt.show()
# 线图
plt.plot(x, z)
plt.show()
# 柱形图
# plt.bar([1,2,3],[4,5,6])
plt.bar(x,z)
plt.show()
# 散点图
plt.scatter(x,z)
plt.show()



