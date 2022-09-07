import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
# import os
pd.set_option('display.max_columns', None)

#outliers

##### Read data from Excel file
dat1=pd.read_excel(r"C:\Users\sarah\Downloads\Table11.xls", index_col=1, header=0)
print(dat1.head(10))
print(dat1.tail(10))
rows, columns = dat1.shape
print(rows, columns)
print(dat1.dtypes)

##### Delete blank columns
dat1=dat1.dropna(axis='columns',how="all") #delet column if all cells are empty
print(dat1)

##### Check blank cells
sb.heatmap(dat1.isnull(),yticklabels=False, annot=True)
plt.show()
plt.clf()

##### Remove duplicates
df=dat1.drop_duplicates()
print(df)
rows, columns = df.shape
print(rows,columns)

##### Fill no data cells with NaN so that dtype issue is resolved
df=df.replace({'na':np.nan,'Na':np.nan, '':np.nan})
print(df.dtypes)

##### Check no data cells
sb.heatmap(df.isnull(),yticklabels=False, annot=True)
plt.show()
plt.clf()

##### Delete rows with no data
df=df.dropna(how="all")
print(df)
#df=df.fillna("NaN")
#print(df)

##### Statistical analysis of data
a1=df.describe()
print(a1)

##### Check no data cells
sb.heatmap(df.isnull(),yticklabels=False, annot=True)
plt.show()
plt.clf()

##### Checks for no data for different columns
a2=df.isnull().sum()
print(a2)
a3=df.isnull().any()
print(a3)

##### Checks data ranges
min=df.min()
max=df.max()
print(min)
print(max)

a2 = df.corr()
print(a2)