import shelve

shelf_file = shelve.open('fav_color.txt')
favorite_color = shelf_file.get('color')
if favorite_color:
    print(f'Your favorite color is {favorite_color}')
else:
    favorite_color = input('Please enter your favorite color: ')
    shelf_file['color'] = favorite_color

shelf_file.close()
