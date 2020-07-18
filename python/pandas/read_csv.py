import pandas as pd

df = pd.read_csv('../data/csvdemo.csv', names=['ID', 'Value'], index_col='ID')
print('DataFrame:\n', df)
print('df.index.name:', df.index.name)