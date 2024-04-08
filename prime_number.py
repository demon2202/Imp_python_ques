def is_prime(x):
    for i in range(2,x):
        if(x%i==0):
         return False
        else:
          return True

x=int(input("enter a number :"))
if is_prime(x):
    print(f"{x} is a prime number.")
else:
    print(f"{x} is not a prime number.")
