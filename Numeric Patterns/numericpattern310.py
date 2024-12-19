height = int(input())

for i in range(0,height):

    for j in range(0,height):
    
        if(i == height-1 or j == height//2):
            print("*",end=" ")
        elif(j == height//2-i-1):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
    
# Sample Input :- 5
# Output :-
#   * *
# *   *
#     *
#     *
# * * * * *
