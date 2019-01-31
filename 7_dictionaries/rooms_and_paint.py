""" Example dictionary operations """

paint_colors = {
    'Kitchen': 'blue',
    'Living Room': 'green',
    'Bedroom': 'purple',
    'Bathroom': 'blue'
}

print('Rooms to paint:', paint_colors)

# painted the bedroom
bedroom_color = paint_colors.pop('Bedroom')
print('Painted the bedroom', bedroom_color)

print('Rooms left to paint:', paint_colors)

# Need to paint the hallway
print('Need to paint the hallway')
paint_colors['Hallway'] = 'Beige'
print('Rooms left to paint:', paint_colors)

# What color was the kitchen supposed to be?
kitchen_color = paint_colors['Kitchen']
print('The kitchen will be painted ' + kitchen_color)

