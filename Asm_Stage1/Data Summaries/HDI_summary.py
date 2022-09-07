import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt

df = pd.read_excel(r"C:\Users\sarah\Uni\DATA1002\Table_1_Cleaned.xlsx", index_col=1, header=0)

# Statistical analysis of data
a1 = df.describe()
print(f'\nAGGREGATE SUMMARIES:\n{a1}')

#Check no data cells
sb.heatmap(df.isnull(), yticklabels=False, annot=True)
plt.show()
plt.clf()

#Checks data ranges
min = df.min()
max = df.max()
print(f'\nMINIMUM VALUES: \n{min}')
print(f'\nMINIMUM VALUES: \n{max}')

a2 = df.corr()
print(f'\nCORRELATION MATRIX:\n{a2}')