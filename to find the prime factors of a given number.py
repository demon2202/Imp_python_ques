x=int(input("Enter a number :"))
y=[]
for i in range(2,x):
  if x%i==0:
    y.append(i)
print(y)
