n=4
for i in range(n+1):
    if i == 0:
      print("*" * n)  # Print full line
    else:
      print(" "*(n-i),end="") 
      print("*")

# ****
#    * 
#   * 
#  * 
# *
