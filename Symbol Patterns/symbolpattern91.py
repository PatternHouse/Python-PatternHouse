main_diagonal = int(input())

for i in range(2 * main_diagonal + 2):
    if i == 0 or i == 2 * main_diagonal + 1:
        for j in range(main_diagonal):
            print(' ', end="")
        print('*', end="")
    
    else:
        if i <= main_diagonal:
            for j in range(main_diagonal - i):
                print(' ', end="")
            print('/', end="")
            for j in range(2 * i - 1):
                print(' ', end="")
            print('\\', end="")
        else:
            n = -i + 2 * main_diagonal + 1
            for j in range(main_diagonal - n):
                print(' ', end="")
            print('\\', end="")
            for j in range(2 * n - 1):
                print(' ', end="")
            print('/', end="")
    print('\n', end="")

# EXAMPLE: 4
#    *
#   / \
#  /   \
# /     \
#/       \
#\       /
# \     /
#  \   /
#   \ /
#    *
