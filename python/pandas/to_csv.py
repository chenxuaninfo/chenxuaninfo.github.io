import pandas as pd

# 生成一些数据
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)  # 将字典转化为dataframe格式
print(df)  # 打印dataframe

# 进行一些操作
df['A'] = df['A']+1

# 存储为csv文件
df.to_csv('../data/csvdemo.csv', index=None)
# df.to_csv('../data/csvdemo.csv', index=None, mode='a', header=False)
# df.to_csv('../data/csvdemo.csv', index=None, mode='a', header=False)