import openpyxl

workbook = openpyxl.load_workbook('ITEC_Courses.xlsx')

# Workbooks are composed of sheets
sheet_names = workbook.sheetnames
print(sheet_names)

first_sheet = workbook.active

# Get all the rows from the sheet
rows = first_sheet.rows

# Looping over rows
for row in rows:
    # looping over every cell in a row
    for cell in row:
        print(cell.value)


# Get all the columns from the sheet
columns = first_sheet.columns

# Loop over all columns
for col in columns:
    # loop over every cell in the column
    for cell in col:
        print(cell.value)


# Getting individual cell data
b2_data = first_sheet['B2'].value  # The data in cell B2
print(f'Cell B2 contains {b2_data}')  # 1100

c5_data = first_sheet['C5'].value
print(f'Cell C5 contains {c5_data}')


# Looping over all of the data in a column

# Convert the columns to a list
columns_list = list(first_sheet.columns)

# Get the column we are interested in - the
# second column (index 1) contains class codes
class_code_column = columns_list[1]

# Loop over, as before
for code_cell in class_code_column:
    print(code_cell.value)

