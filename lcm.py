def lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while(True):
        if (greater%x==0) and (greater%y==0):
            lcm=greater
            break
        greater+=1
    return lcm

x=int(input("enter a number :")) 
y=int(input("enter a number :"))
print(lcm(x,y))
