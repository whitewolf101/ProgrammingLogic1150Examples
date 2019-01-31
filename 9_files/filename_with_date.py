from datetime import datetime


print(datetime.now())
now = datetime.now()
now_string = now.strftime("%d_%h_%y_%I_%M%p")
print(now_string)

with open(now_string + '.txt', 'w') as f:
    f.write('hello')