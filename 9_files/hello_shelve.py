import shelve

# Write to shelf file

shelf_file = shelve.open('fav_color.txt')
shelf_file['color'] = 'blue'
shelf_file.close()


# Read from shelf file

shelf_file = shelve.open('fav_color.txt')
fav_color = shelf_file['color']
print(f'The user\'s favorite color is {fav_color}')
shelf_file.close()


