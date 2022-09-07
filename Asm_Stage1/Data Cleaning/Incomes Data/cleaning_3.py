missing_values = 0
default_values = 0
alpha_fail = 0
numeric_fail = 0

for line in open("Incomes_Data_CLEANED.csv"):
  line_1 = line.rstrip()
  edited_list = line_1.split(";")

  for word in edited_list:
    if word == "null":
      default_values += 1
    if len(word) > 0 and len(edited_list) == 6:
      for letter in edited_list[0]:
        if letter.isnumeric():
          alpha_fail += 1
      for letter in edited_list[1]:
        if letter.isnumeric():
          alpha_fail += 1
      for letter in edited_list[2]:
        if letter.isnumeric():
          alpha_fail += 1
      if edited_list[-1].isnumeric():
        if int(edited_list[-1]) >= 0:
          numeric_fail += 0
        else:
          numeric_fail += 1
      else:
        numeric_fail += 1
      if edited_list[-2].isnumeric():
        if int(edited_list[-2]) >= 0:
          numeric_fail += 0
        else:
          numeric_fail += 1
      else:
        numeric_fail += 1
      if edited_list[-3].isnumeric():
        if int(edited_list[-3]) >= 0:
          numeric_fail += 0
        else:
          numeric_fail += 1
      else:
        numeric_fail += 1
    else:
      missing_values += 1
      
# Results of quality checks:

if missing_values == 0:
  print("PASSED TEST 1 - There are no missing values.")
else: 
  print("FAILED TEST 1 - There are still missing values in the dataset.")
  
if default_values == 0:
  print("PASSED TEST 2 - There are no default values.")
else: 
  print("FAILED TEST 2 - There are still default values in the dataset.")

if numeric_fail == 0:
  print("PASSED TEST 3 - All income fields are numeric and non-negative.")
else:
  print("FAILED TEST 3 - Not all income fields are numeric and non-negative.")

if alpha_fail == 0:
  print("PASSED TEST 4 - Text fields contain only alphabetic and special characters.")
else: 
  print("FAILED TEST 4 - Not all text fields contain only alphabetic and special characters.")
  
if missing_values > 0:
  print("---------")
  print("  Note: Tests 3 and 4 cannot be conducted on rows with missing values.")
  print("        Please rectify missing values and re-run tests.")
