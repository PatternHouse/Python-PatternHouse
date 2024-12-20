side_size = int(input())

for i in range(side_size):
    for j in range(side_size):
        print(max(i,j)+1, end=' ')
    print('\n', end='')
        

#EXAMPLE:
# side_size = 5:
#1 2 3 4 5
#2 2 3 4 5
#3 3 3 4 5
#4 4 4 4 5
#5 5 5 5 5
