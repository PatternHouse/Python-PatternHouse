import math

side_size = int(input())
prime_numbers = 0
i = 2
print_n = 0

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False;
    
    return True;

while(prime_numbers < side_size ** 2):
    if(is_prime(i)):
        prime_numbers += 1;
        print_n = 1
        print(i, end=' ')
        
    if(prime_numbers % 5 == 0 and prime_numbers != 0 and print_n):
        print('\n', end='')
        print_n = 0
    
    i += 1

# EXAMPLE:
# 5:
#2 3 5 7 11
#13 17 19 23 29
#31 37 41 43 47
#53 59 61 67 71
#73 79 83 89 97
