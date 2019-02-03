from datetime import datetime


now = datetime.now()
now_string = now.strftime("%d_%h_%y_%I_%M%p")

with open(now_string + '.txt', 'w') as f:
    f.write('hello')
