import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import os
import xlsxreader
import xlsxwriter
import xlwt

pd.set_option('display.max_columns', None)

def clean(dat1):
    # Delete blank columns
    dat1 = dat1.dropna(axis='columns',how="all")
    print(dat1)

    # Check blank cells
    sb.heatmap(dat1.isnull(),yticklabels=False, annot=True)
    plt.show()
    plt.clf()

    #Remove duplicates
    df = dat1.drop_duplicates()
    print(df)
    rows, columns = df.shape
    print(rows,columns)

    #Fill no data cells with NaN so that dtype issue is resolved
    #df=df.replace({'':np.nan})
    print(df.dtypes)

    #Check no data cells
    sb.heatmap(df.isnull(), yticklabels=False, annot=True)
    plt.show()
    plt.clf()

    #Delete rows with no data
    df = df.dropna(how="all")
    print(df)
    #df=df.fillna("NaN")
    #print(df)

    #statistical analysis of data
    a1 = df.describe()
    print(a1)

    #Check no data cells
    sb.heatmap(df.isnull(), yticklabels=False, annot=True)
    plt.show()
    plt.clf()

    #Checks for no data for different columns
    a2=df.isnull().sum()
    print(a2)
    a3=df.isnull().any()
    print(a3)

    #Checks data ranges
    min=df.min()
    max=df.max()
    print(min)
    print(max)
    return df

# Read data from Excel file
d1 = pd.read_excel(r'C:\Users\sarah\Downloads\Happiness.xls', 'HDI', index_col=0, header=0)
d1 = clean(d1)
d1 = d1.sort_values(by="Country", ascending=True)
print(d1.tail(5))
rows, columns = d1.shape
print(rows, columns)
print("*******************")

d2 = pd.read_excel(r'C:\Users\sarah\Downloads\Happiness.xls', 'Income', index_col=0, header=0)
d2 = clean(d2)
d2 = d2.sort_values(by="Country", ascending=True)
#print(d2.tail(5))
#rows, columns = d2.shape
#print(rows, columns)

d3 = pd.read_excel(r'C:\Users\sarah\Downloads\Happiness.xls', 'Happiness', index_col=1, header=0)
#d3=clean(d3)
d3 = d3.sort_values(by="Country", ascending=True)
#print(d3.tail(5))
#rows, columns = d3.shape
#print(rows, columns)

d4 = pd.merge(d3[['Happiness2021', 'HappinessRank', 'Pop2022']], d1, left_on='Country', right_on='Country', how='left')
d5 = pd.merge(d4, d2[['Income2020', 'Region']], left_on='Country', right_on='Country', how='left')

df = clean(d5)

print('===========')
print(df.tail(5))
rows, columns = df.shape
print(rows, columns)
print('===========')

df.to_excel('Happy_Res.xls')

# Correlation
# df = df.dropna(axis='columns', how="region")
cor = df.corr()
print(cor)