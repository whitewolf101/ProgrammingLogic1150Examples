import openpyxl

workbook = openpyxl.load_workbook('ITEC_Courses.xlsx')

# Workbooks are composed of sheets
sheet_names = workbook.sheetnames
print(sheet_names)

names_sheet = workbook.active

# Getting individual cell data
b2_data = names_sheet['B2'].value  # The data in cell B2
print(f'Cell B2 contains {b2_data}')  # 1100

c5_data = names_sheet['C5'].value
print(f'Cell C5 contains {c5_data}')  # Microsoft Windows Operating Systems


# Get all the rows from the sheet
rows = names_sheet.rows

# Looping over rows
for row in rows:
    # looping over every cell in a row
    for cell in row:
        print(cell.value)


# Get all the columns from the sheet
columns = names_sheet.columns

# Loop over all columns
for col in columns:
    # loop over every cell in the column
    for cell in col:
        print(cell.value)



# Looping over all of the data in a column

# Convert the columns to a list
columns_list = list(names_sheet.columns)

# Get the column we are interested in - the
# third column (index 2) contains class names
class_code_column = columns_list[2]

# Loop over, as before. Print all class names
for code_cell in class_code_column:
    print(code_cell.value)


# Get the other sheet - need to get by name
# Syntax looks like reading from a dictionary
rooms_sheet = workbook['rooms']
rooms_columns = rooms_sheet.columns

for column in rooms_columns:
    for cell in column:
        print(cell.value)

