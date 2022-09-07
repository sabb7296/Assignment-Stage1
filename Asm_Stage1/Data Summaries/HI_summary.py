import pandas as pd
df = pd.read_csv('HappinessIndex.csv')
dff = pd.DataFrame(df)

#Country with largest population
col = "pop2022"
max_pop = dff.loc[dff[col].idxmax()]
print("Country with the largest population and its corresponding rank, happines index in 2020 and 2021: ")
print( max_pop)

#Country with smallest population
col = "pop2022"
min_pop = dff.loc[dff[col].idxmin()]
print("Country with the smallest population and its corresponding rank, happines index in 2020 and 2021: ")
print( min_pop)

#Average happiness index in each year
#2020
df1 = dff["happiness2020"].mean()
print ("The average happiness index in 2020 is " ,df1)

#2021
df2 = dff["happiness2021"].mean()
print ("The average happiness index in 2021 is " ,df2)






