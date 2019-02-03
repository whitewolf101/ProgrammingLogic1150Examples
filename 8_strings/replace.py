""" replace function replaces one string with another """

message = 'The student is taking itec 1150 and itec 1310.'
corrected = message.replace('itec', 'ITEC')
print(corrected)

student_email = 'ab1234cd@go.minneapolis.edu'
student_star_id = student_email.replace('@go.minneapolis.edu', '')
print(student_star_id)

excited = 'Hi!!!!! can you help!!!! I need coffee!!!!!'
calm = excited.replace('!', '')
print(calm)


