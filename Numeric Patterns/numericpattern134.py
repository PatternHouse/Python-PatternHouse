print("Enter the number:")
n=int(input())

for i in range(0,n,2):
  for j in range(1,n+1):
    print(n*i+j,end=" ")
  print()

if(n%2==1):
  for i in range(n-2,0,-2):
    for j in range(1,n+1):
      print(n*i+j,end=" ")
    print()
else:
  for i in range(n-1,0,-2):
    for j in range(1,n+1):
      print(n*i+j,end=" ")
    print() 
    
Enter the no of rows: 
5
1 2 3 4 5
11 12 13 14 15
21 22 23 24 25
16 17 18 19 20 
6 7 8 9 10
