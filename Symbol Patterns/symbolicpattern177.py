n=5
for i in range(n):
    if i == 0 or i == n - 1 or i==n//2:
      print("*" * n)  # Print full line
    elif(i<n//2):
      print("*"+n*" ")  # Hollow line
    else:
      print("*"+(n-2)*" "+"*") 

# output
# *****
# *     
# *****
# *   *
# *****
