import csv
import pandas as pd
import numpy as np

df1 = pd.read_csv("/home/qiaoqiao/Desktop/basketball/CSP571/Team_Ranks/rank_result_cleaned.csv")
df2 = pd.read_csv("/home/qiaoqiao/Desktop/basketball/CSP571/final1.csv")

df3 = df1.merge(df2, on=["Name","season"], how='outer')
df3.to_csv("/home/qiaoqiao/Desktop/basketball/CSP571/final2.csv",index=False)