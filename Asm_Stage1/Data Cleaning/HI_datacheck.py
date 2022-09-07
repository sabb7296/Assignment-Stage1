import pandas as pd
df = pd.read_csv('HappinessIndex.csv')


#Checking if there are any cells with no data 
#total cells without data
cells =df.isnull().sum()
print(cells)
#checking individual cells
cell =df.isnull().any()
print(cell)

#Deleting duplicates
d1=df.drop_duplicates()
print(d1)
rows, columns = d1.shape
print(rows,columns)

#Checking type of the data in each column
type = df.dtypes
print(type)

#Checking for missing values
print (df.isnull())





