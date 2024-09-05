print('\033c')

def is_prime(n):
    
    if n <= 1:
        return False
    
    for i in range(2,num):
  
        
        if n % i == 0:
            return False
        return True

num = int(input("Enter the number:"))

if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")