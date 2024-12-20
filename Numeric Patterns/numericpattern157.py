side_size = int(input())

for i in range(side_size):
    for j in range(side_size):
        print(min(j+1, side_size-i), end=' ')
    print('\n', end='')

# EXAMPLE:
# 5:
#1 2 3 4 5
#1 2 3 4 4
#1 2 3 3 3 
#1 2 2 2 2
#1 1 1 1 1
