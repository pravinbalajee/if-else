a=int(input("enter a 1st number : "))
b=int(input("enter a 2nd number :"))
sub =("-")
add=("+")
div=("/")
x=input("enter a symbol : ")
if x==sub:
    print("subtraction of two number is",a-b)
elif x==add:
    print("addition of two numbers is",a+b)
elif x==div:
    print("the division of two numbers is",a/b)
else:
    print("the multiplication of two numbers is",a*b)