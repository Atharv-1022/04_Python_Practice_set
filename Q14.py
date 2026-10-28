'''Write a function safe_divide(a, b) that returns the result of a / b, but returns "Cannot divide by zero" if b is 0'''
def safe_divide(a,b):
    if b==0:
        return "Cannot divide by 0"
    else:
        return a/b
num1=int(input("Enter the first number:"))
num2=int(input("Enter the Second number:"))

print(safe_divide(num1,num2))