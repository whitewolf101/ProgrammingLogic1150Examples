""" Getting keys, or values, or all the pairs from a dictionary
These methods all return things you can loop over, and use the same methods we used on lists """

games_and_publishers = {'Minecraft': 'Mojang', 'Overwatch': 'Blizzard', 'Fortnight': 'Epic'}

video_games = games_and_publishers.keys()
print(video_games)  # dict_keys(['Minecraft', 'Overwatch', 'Fortnight'])

publishers = games_and_publishers.values()
print(publishers)  # dict_values(['Mojang', 'Blizzard', 'Epic'])

key_values = games_and_publishers.items()
print(key_values)  # dict_items([('Minecraft', 'Mojang'), ('Overwatch', 'Blizzard'), ('Fortnight', 'Epic')])

# Can treat like a list in many ways  - can use len(), sum() for numbers, and loop over them

for p in publishers:
    print(p)

print(f'There are {len(publishers)} publishers.')


# To use list methods, have to turn them into a list, and then use list methods like sort, or reverse
video_games_list = list(video_games)
video_games_list.sort()
print(video_games_list)

publishers_list = list(publishers)
publishers_list.reverse()
print(publishers_list)


# Another example with numeric keys

sales = {'Monday': 145, 'Tuesday': 234, 'Wednesday': 198}
quantities = sales.values()
total = sum(quantities)
print('Total items sold:', total)

