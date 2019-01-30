"""
Making a to do list in Python using a while loop to get
the tasks, and a for loop to print all the tasks.
This version uses enumerate() to display a numbered task list.
"""

todo_list = []  # Make an empty list

while True:
    task = input('Enter your task, or press enter to stop: ')
    if task:
        todo_list.append(task)
    else:
        break

print('Thank you. Your tasks are:')

# Enumerate returns the index of the list item and the list item, one by one.
# Convenient if you need to know where you are in the list,
# as well as the data from the list
for index, task in enumerate(todo_list):
    print(f'Task {index+1} is {task}')

