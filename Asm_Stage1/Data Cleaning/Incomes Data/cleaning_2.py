
for line in open("Incomes_Data1.csv"):
  default_values = 0
  list_1 = line.rstrip()
  list = list_1.split(";")
  edited_list = [list[0], list[1], list[2], list[-3], list[-2], list[-1]]
 
  for word in edited_list:
    if word == "null" or word == '"null' or word == 'null"':
      default_values += 1
  
  if default_values == 1:
    if edited_list[1] == "High income":
      percent_change = 1 - 0.0679
      edited_list[-1] = str(int(float(edited_list[-2])* percent_change))
    elif edited_list[1] == "Upper middle income":
      percent_change = 1 - 0.0888
      edited_list[-1] = str(int(float(edited_list[-2])* percent_change))
    elif edited_list[1] == "Lower middle income":
      percent_change = 1 - 0.0535
      edited_list[-1] = str(int(float(edited_list[-2])* percent_change))
    elif edited_list[1] == "Low income":
      percent_change = 1 - 0.0323
      edited_list[-1] = str(int(float(edited_list[-2])* percent_change))
    
  if not "null" in edited_list:
    final_file = ";".join(edited_list)
    if '"' in final_file:
      final_file = final_file.rstrip('"')
      final_file = final_file.lstrip('"')
    print(final_file)
    
    
    
