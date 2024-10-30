for i in range(5):
  for j in range(5):
    if((i+j)%2==1 and i!=0 and j!=0 and i!=4 and j!=4):
      print(0, end=" ")
    else:
      print(1,end=" ")
  print()

# 1 1 1 1 1 
# 1 1 0 1 1 
# 1 0 1 0 1 
# 1 1 0 1 1 
# 1 1 1 1 1 
