nterms = int(input("How many terms the user wants to print? "))


n1 = 0
n2 = 1
count = 0

if nterms <= 0:
    print("Please enter a positive integer, the given number is not valid")
# if there is only one term, it will return n_1
elif nterms == 1:
    print("The Fibonacci sequence of the numbers up to", nterms, ": ")
    print(n1)

else:
    print("The fibonacci sequence of the numbers is:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1