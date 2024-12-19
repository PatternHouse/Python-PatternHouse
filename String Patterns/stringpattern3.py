print('Enter a string')
pattern_string = input()
for i in range (len(pattern_string)) :
  for ch in pattern_string [0:i+1] :
    print(ch, end =' ')
  print()  
