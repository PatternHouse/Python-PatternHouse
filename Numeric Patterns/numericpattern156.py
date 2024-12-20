side_size = int(input())

for i in range(side_size):
    for j in range(side_size):
        print(min(i, j)+1, end=' ')
    print('\n', end="")

# EXAMPLE:
# side_size = 5
#1 1 1 1 1 
#1 2 2 2 2
#1 2 3 3 3
#1 2 3 4 4
#1 2 3 4 5
