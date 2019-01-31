""" Looping over a dictionary examples """

classes = {
    1150: 'Programming Logic',
    1425: 'Data Communications',
    1310: 'PC Maintenance'
}

# Looping over a dictionary - by default, loop over keys
for class_code in classes:
    print(class_code)


# To loop over the values, use the values() function
for class_name in classes.values():
    print(class_name)


# And to loop over both at once, use the items() function
for class_code, class_name in classes.items():
    print(f'ITEC {class_code} is {class_name}')

