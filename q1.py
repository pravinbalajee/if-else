a=int(input("enter a number:"))
b=int(input("enter a number:"))
if (a+b>=50):
    print("the given sum is",a,b,"is",a+b,"which is <50",True)
    if (a+b<=50):
        print("the sum of",a,"+",b,"is",a+b,"which is greater than or equal to 50",True)
else:
    print("the sum of",a,"+",b,"is",a+b,"which is less than 50",False)