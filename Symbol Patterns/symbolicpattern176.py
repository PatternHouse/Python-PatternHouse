n=5
for i in range(n):
    if i == 0 or i == n - 1 or i==n//2:
      print("*" * n)  
    elif(i<n//2):
      print("*"+n*" ") 
    else:
      print((n-1)*" "+"*") 

# output
# *****
# *     
# *****
#     *
# *****

