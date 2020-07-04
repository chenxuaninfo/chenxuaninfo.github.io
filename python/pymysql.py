# 导入pymysql
import pymysql

# 建立连接
conn = pymysql.connect(host='localhost',user='root',password='root',db='school_kettle',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

# 建立游标
cur = conn.cursor()

# 执行SQL
cur.execute("select * from users;")

# 打印结果
for row in cur:
    print(row)

# 关闭游标
cur.close()

# 关闭连接
conn.close()