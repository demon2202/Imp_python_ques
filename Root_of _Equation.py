#quadratic equation ax**2 + bx + c = 0 
a=int(input("enter the valve of a :"))
b=int(input("enter the value of b :"))
c=int(input("Enter the value of c :"))
q= (b**2 - 4*a*c)**(1/2)
d=(-b+q)/2*a
d2=(-b-q)/2*a
print("First root is :",d,"\n","Second root is :",d2)