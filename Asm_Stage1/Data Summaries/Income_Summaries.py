# Number of countries in each income group.
country_count = {}
line_count = -1

for line in open("Incomes_Data_CLEANED.csv"):
  line_count += 1
  if line_count > 0:
    values = line.rstrip().split(";")
    category = values[1]
    if category not in country_count:
      country_count[category] = 1
    else:
      country_count[category] += 1
      
print("Number of countries in each income group:")
for category in sorted(country_count):
  print(category + " = " + str(country_count[category]))
  
# Highest and lowest incomes (with year and country name).
print("----------")
country_income = {}
line_count_1 = -1

for line_1 in open("Incomes_Data_CLEANED.csv"):
  line_count_1 += 1
  if line_count_1 > 0:
    values_1 = line_1.rstrip().split(";")
    country = values_1[0]
    tuple_1 = ("2018, " + country)
    tuple_2 = ("2019, " + country)
    tuple_3 = ("2020, " + country)
    if not tuple_1  in country_income:
      country_income[tuple_1] = int(values_1[-3])
    if not tuple_2  in country_income:
      country_income[tuple_2] = int(values_1[-2])
    if not tuple_3 in country_income:
      country_income[tuple_3] = int(values_1[-1])

max_income = -1
min_income = 1000000000
for key in country_income:
  max_income = max(max_income, country_income[key])
  min_income = min(min_income, country_income[key])
for key in sorted(country_income):
  if country_income[key] == max_income:
    print("Highest income in dataset occured in "+ key + " : " + str(max_income))
  if country_income[key] == min_income:
    print("Lowest income in dataset occured in "+ key + " : " + str(min_income))

# Average income per group for each year.
line_count = -1
avg_income_2018 = {}
avg_income_2019 = {}
avg_income_2020 = {}

for line in open("Incomes_Data_CLEANED.csv"):
  line_count += 1
  if line_count > 0:
    values_2 = line.rstrip().split(";")
    group = values_2[1]
    income_2018 = float(values_2[-3])
    income_2019 = float(values_2[-2])
    income_2020 = float(values_2[-1])
    if group not in avg_income_2018:
      avg_income_2018[group] = [income_2018]
    else:
      avg_income_2018[group].append(income_2018)
    if group not in avg_income_2019:
      avg_income_2019[group] = [income_2019]
    else:
      avg_income_2019[group].append(income_2019)
    if group not in avg_income_2020:
      avg_income_2020[group] = [income_2020]
    else:
      avg_income_2020[group].append(income_2020)

print("----------")
print("Average incomes of each group in 2018:")
for key in sorted(avg_income_2018):
  mean = int(sum(avg_income_2018[key])/len(avg_income_2018[key]))
  print(key + " = " + str(mean))
  
print("----------")
print("Average incomes of each group in 2019:")
for key in sorted(avg_income_2019):
  mean = int(sum(avg_income_2019[key])/len(avg_income_2019[key]))
  print(key + " = " + str(mean))

print("----------")
print("Average incomes of each group in 2020:")
for key in sorted(avg_income_2020):
  mean = int(sum(avg_income_2020[key])/len(avg_income_2020[key]))
  print(key + " = " + str(mean))
