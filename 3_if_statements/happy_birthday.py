"""
An if-statement that does a task if a condition is true.
If the condition is not true, the task is skipped.
"""


current_month = 'February'  # TODO change this to the current month

birthday_month = input('What month were you born in? ')

if birthday_month == current_month:
    # your birthday is this month
    print('Happy birthday month!')

# otherwise, your birthday is not this month.

print('Thank you for running this program!')  # this always prints