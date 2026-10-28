# Write a recursive function sum_of_digits(n) that returns the sum of all digits of a given number
def sum_digit(n):
    if n==1:
        return 1
    return sum_digit(n-1)+n

print(sum_digit(5))