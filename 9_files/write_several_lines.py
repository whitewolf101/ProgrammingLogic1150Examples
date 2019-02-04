""" Write lines to a file """


f = open('planets.txt', 'w')  # 'w' for write mode
f.write('Hello Venus\n')
f.write('Hello Mars\n')
f.close()

