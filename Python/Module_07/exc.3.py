def largest(a,b,c):
    if a>b and a>c:
        return "a is greater"
    elif b>c:
        return "b is greater"
    else:
        return "c is greater"
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
z=int(input("Enter third number:"))
greatest=largest(x,y,z)
print("The greatest among three number is:",greatest)