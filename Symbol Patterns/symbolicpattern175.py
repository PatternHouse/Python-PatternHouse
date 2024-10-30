n=int(input())
if(n%2==0):
  m=n+1
else:
  m=n
for i in range(m):
  if(i<n//2):
    for i in range(n):
      if(i==0 or i==n-1): 
        print("*",end="")
      else:
        print("",end=" ")     
  elif(i==n//2):
    for i in range(n):
      print("*",end="")
  else:
    for i in range(n):
      if(i==n-1):
        print("*",end="")
      else:
        print(" ",end="")
  print()
# sample output
# 11
# *         *
# *         *
# *         *
# *         *
# *         *
# ***********
#           *
#           *
#           *
#           *
#           *

