import pymysql
# 打开数据库连接
db = pymysql.connect("localhost","root","root","employees" )
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
# SQL 查询语句
sql = """
WITH tx as (
SELECT
	salaries.salary,
	count( salaries.salary ) AS num 
FROM
	salaries 
GROUP BY
	salaries.salary
)
SELECT
	salary,
	PERCENT_RANK() OVER (ORDER BY num ) AS WIN_PERCENT_RANK,
	NTILE(10) OVER ( ORDER BY num )  AS WIN_NTILE 
FROM
	tx
limit  10
"""

try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   # 打印
   for row in results:
        for t in row:
            print (t)
except:
   print ("Error: unable to fetch data")
 
# 关闭数据库连接
db.close()


