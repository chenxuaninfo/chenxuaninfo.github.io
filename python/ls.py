# import pandas as pd
# import numpy as np

# 读取文件
# df = pd.read_csv('Transactions.csv')
# 查看前5行
# df.head()
# 查看数据集大小（x,y）
# df.shape
# 字段类别
# df.info()
# 描述统计
# df.describe()

# 查看数据集重复值
# df.duplicated().sum()
# 查看所有行重复值
# df[df.duplicated()==True]
# 删除重复数据
# dfn = df.drop_duplicates()

# 缺失值处理(检查空值)
# df.isnull().sum()
# 查看所有缺失值
# df[df.isnull().T.any()]
# 缺失值填充0
# df=df.fillna(0)
# df.isnull().any()


# 数据排序
# df.sort_values(by = ['tran_date'],ascending = True,inplace=True)


# 异常值处理
# df['Qty'].isin([0]).sum()
# df['Rate'].isin([0]).sum()
# df['Rate'].isin([0]).sum()
# df['total_amt'].isin([0]).sum()


# 另存为新的文件
# df.to_csv('Transactions_dis.csv', index=None)


