""" Split a list of emails and verify that they are all student emails """

emails = 'aa1111aa@go.minneapolis.edu;bb2222bb@go.minneapolis.edu;not.a.student@gmail.com;cc3333cc@go.minneapolis.edu'

email_list = emails.split(';')

for email in email_list:
    if email.endswith('.edu'):
        print(f'{email} is a student email')
    else:
        print(f'{email} is NOT a student email!')


