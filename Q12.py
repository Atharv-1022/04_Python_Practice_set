'''Write a function multiply(a, b) that has a proper docstring explaining what it does. Then use help(multiply) to display the docstring.
'''
def multipye(a,b):
    '''it is mutiplicastion program
    first it takes a as num1
    then it takes b as num2
    then dose the multiplcastion by given comand a*b by putting values on ther place
    and returns the ans when it is called
    '''
    return a*b

print(multipye.__doc__)
print(multipye(2,3))
