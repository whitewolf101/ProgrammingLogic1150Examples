"""
Hockey games

if the Minnesota Wild score 2
The Detroit Red Wings score 3

Who won?

Substitute your teams of your choice if preferred. Or baseball/basketball/soccer/other sport.

"""

minnesota_wild_score = 2
detroit_red_wings_score = 20

if detroit_red_wings_score % 10 == 0:   # true if score is 10 or 20 or 30 ...
    print('The score is a multiple of 10')

if minnesota_wild_score > detroit_red_wings_score:
    print('Minnesota Wild won')
elif detroit_red_wings_score > minnesota_wild_score:  # else if
    print('Detroit Red Wings won')
else:
    print('The game is a tie - both teams same score')

print('That\'s the end of the program!')

