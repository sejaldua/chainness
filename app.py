import csv
import pandas as pd

df1 = pd.read_csv('./data/chainness_point_2021_part1.csv')
df2 = pd.read_csv('./data/chainness_point_2021_part2.csv')
df3 = pd.read_csv('./data/chainness_point_2021_part2.csv')

df = pd.concat([df1, df2, df3], axis=0)
print(list(df['Cuisine'].unique()))
