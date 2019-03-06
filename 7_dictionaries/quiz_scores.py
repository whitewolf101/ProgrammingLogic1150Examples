
scores = {'Al': 9, 'Bettina': 7, 'Cody': 6, 'Dora': 10}

# Reading a score
al_score = scores['Al']
print(al_score)  # 9

# Reading a score
dora_score = scores['Dora']
print(dora_score)  # 10

# Changing a score. Cory re-took his quiz
scores['Cody'] = 8
print(scores)  # {'Al': 9, 'Bettina': 7, 'Cody': 8, 'Dora': 10}

# Adding a new score
scores['Edwin'] = 8
print(scores)  # {'Al': 9, 'Bettina': 7, 'Cody': 8, 'Dora': 10, 'Edwin': 8}

# Adding a new score
scores['Freya'] = 9
print(scores)  # {'Al': 9, 'Bettina': 7, 'Cody': 8, 'Dora': 10, 'Edwin': 8, 'Freya': 9}

