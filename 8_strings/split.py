"""
split() and splitlines()
"""

# split() with no arguments splits the string by spaces,
# so can be useful to make a list of words in a sentence
class_description = "Programming Logic introduces students to Python programming."
words = class_description.split()
print(words) # ['Programming', 'Logic', 'introduces', 'students', 'to', 'Python', 'programming.']
print(words[0])  # The first word, 'Programming'


# split() with an argument splits the string by that character
url = 'https://en.wikipedia.org/wiki/Binary_number'
parts = url.split('/')
topic = parts.pop()
print(topic)  # 'Binary_number'

# split() with an argument that isn't in the string results in a list of one item - the entire original string
message = 'No dollar signs in this string.'
split_by_dollar = message.split('$')
print(split_by_dollar)  # ['No dollar signs in this string.']



letter = """Dear students,
Thank you all for coming to Advising Day this year. It was great to have 
you, and the employers who visited enjoyed meeting you all.
We hope you found the event useful, and made some good connections. 
All the best,
The ITEC department.
"""

lines = letter.splitlines()
print(lines)
