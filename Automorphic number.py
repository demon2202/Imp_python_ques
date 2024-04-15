#Explanation : Number = 5
#Square of number = 25
#as the square of the number ends with the number itself, It's an Automorphic number.

number = 376
square = pow(number, 2)
mod = pow(10, len(str(number)))

if square % mod == number:
    print("It's an Automorphic Number")
else:
    print("It's not an Automorphic Number")
