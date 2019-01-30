""" pop removes the last item, or the item at a particular index.
pop returns the item that was removed
You can ignore the item, if you don't need it, or use it if you do.
"""

colleges = ['Minneapolis College',
            'Metro State',
            'Saint Paul College',
            'North Hennepin Community College',
            'Century College']

# Remove the last list item. Use pop with no arguments.
last_college = colleges.pop()  # 'Century College'
print(last_college)
print(colleges)   # ['Minneapolis College', 'Metro State', 'Saint Paul College', 'North Hennepin Community College']

# Remove the item at an index - use pop with that index
second_college = colleges.pop(1)
print(second_college)  # Metro State
print(colleges)    # ['Minneapolis College', 'Saint Paul College', 'North Hennepin Community College']

# You can ignore the item, if you don't need it. Perhaps you know you don't need element 0 any more.
colleges.pop(0)
print(colleges)  # ['Saint Paul College', 'North Hennepin Community College']
