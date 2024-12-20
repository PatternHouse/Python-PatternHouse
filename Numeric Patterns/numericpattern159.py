side_size = int(input())

for i in range(side_size):
    for j in range(side_size-i):
        print(side_size-i, end=' ')
    for j in range(side_size-i, side_size):
        print(j+1, end=' ')
        
    print('\n', end='')
        

#EXAMPLE:
#side_size = 5:
#5 5 5 5 5
#4 4 4 4 5
#3 3 3 4 5
#2 2 3 4 5
#1 2 3 4 5
