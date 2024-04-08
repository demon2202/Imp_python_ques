x=int(input("enter a number :"))
t=x
sum=0
q=len(str(x))
while t>0:
    d=t%10
    sum=pow(d,q)+sum
    t//=10
if sum==x:
    print("The number is armstrong")
else:
    print("Not armstrong")