# Create list using data, then print. 
# Cut to Country, Income Group, Region, (2018-2020) range. 

print("Data Errors:")
row_number = 0
default_values_1 = 0
default_values_extra = 0

for line in open("Incomes_Data1.csv"):
  default_values = 0
  row_number += 1
  list_1 = line.rstrip()
  list = list_1.split(";")
  edited_list = [list[0], list[1], list[2], list[-3], list[-2], list[-1]]
 
  for word in edited_list:
    if not len(word) > 0 or not len(edited_list) == 6:
      print("Row " + str(row_number) + ", " + edited_list[0] + " is missing values.")
    if word == "null" or word == '"null' or word == 'null"':
      default_values += 1
  
  if default_values == 1:
    default_values_1 += 1
  elif default_values >= 2:
    default_values_extra += 1
    
print("There are " + str(default_values_1) + " countries with 1 default value.")
print("There are " + str(default_values_extra) + " countries with 2 or more default values.")