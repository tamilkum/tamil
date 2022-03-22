rows = 5 
for i in range(0,rows):
    for j in range(0,rows -i -1):
        print(end = ' ')
    for k in range(0, i +1):
        print('*',end=' ')
    print()

rows = 5
for i in range(rows, 0, -1):
    for j in range(0, rows-i):
        print(end = ' ')
    for k in range(0, i):
        print('*', end =' ')
    print()





