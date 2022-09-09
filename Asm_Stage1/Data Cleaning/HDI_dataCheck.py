import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from fuzzymatcher import link_table, fuzzy_left_join
import os
import xlsxreader
import xlsxwriter
import xlwt

pd.set_option('display.max_columns', None)

def clean(dat1):
    #Delete blank columns
    dat1 = dat1.dropna(axis='columns', how="all")
    print(dat1)

    # Check blank cells
    sb.heatmap(dat1.isnull(),yticklabels=False, annot=True)
    plt.show()
    plt.clf()

    #Remove duplicates
    df=dat1.drop_duplicates()
    print(df)
    rows, columns = df.shape
    print(rows,columns)

    # Fill no data cells with NaN so the dtype issue is fixed
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

    #Statistical analysis of data
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

    # Checks data ranges
    min=df.min()
    max=df.max()
    print(min)
    print(max)
    return df

# Read HDI data from Excel file
d1 = pd.read_excel(r"C:\Users\sarah\Downloads\Happiness (1).xls", 'HDI', index_col=0, header=0)
d1 = clean(d1)
d1 = d1.sort_values(by="Country1", ascending=True)
print(d1.tail(5))
rows, columns = d1.shape
print(rows, columns)
print("*******************")
d1.to_excel('HDI_cleaned.xls')
