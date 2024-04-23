"""
A
B C
D E F
G H I J
K L M N O
"""
def num(n):
    num = 1
    for i in range(0, n):
        for j in range(0, i+1):
            print(num, end=" ")
            num = num + 1
        print("\r")

n = 5
num(n)
