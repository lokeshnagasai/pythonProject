def factorial(n):

    return 1\
        if (n == 1 or n == 0)  else n * factorial(n - 1)
num = int(input("enter number:"))
print("Factorial of", num, "is", factorial(num))
"""
def fact(n):
    if n>1:
        return n*fact(n-1)
    else:
        return 1
n=int(input("Enter a number: "))
print("factorial of %d is %d"%(n,fact(n)))"""