# Problem statement: Check if a number is prime or not:
# input provided by user: n
# output: 
# n is a Prime number.
# n is not a Prime number.

# take input from user:
n = int(input("Enter a number: "))
print()

# Approach #1: BF(Brute Force):
if n <= 1:
    print(f"BF: n <= 1 : {n} is not a Prime number.")
elif n <= 3:
    print(f"BF: n <= 3 : {n} is a Prime number.")
else:
    for i in range(2,n):
        if n % i == 0:
            print(f"BF: {n} mod {i} = 0 : {n} is not a Prime number.")
            break
        else:
            i+=1
            if (i==n):
                print(f"BF: i = {n} : {n} is a Prime number.")
print()

# Approach #2: BA(Better Approach) : minimize how many times the loop runs:
    # if n is not a prime number then n must
    # be equal to multiplication of two natural numbers in range (2, n-1)
    # Therefore, n = i * b where i,b lies in (2, n-1)
    # then, b = n/i and here, b >= i
    # then, i*b >= i*i  =>  i*b >= i^2
    # then, n >= i^2    (bcoz i*b=n)
    # =>  n^(1/2) >= i
    # this means, we don't need to loop till n-1 rather we can just loop till n**(0.5)
n2=int(n**0.5) + 1
if n <= 1:
    print(f"BA: n <= 1 : {n} is not a Prime number.")
elif n <= 3:
    print(f"BA: n <= 3 : {n} is a Prime number.")
else:
    for i in range(2,n2):
        if n % i == 0:
            print(f"BA: {n} mod {i} = 0 : {n} is not a Prime number.")
            break
        else:
            i+=1
            if (i==n2):
                print(f"BA: i = {n2} : {n} is a Prime number.")
print()

# OUTPUT:
# =======
# Enter a number: 101

# BF: i = 101 : 101 is a Prime number.

# BA: i = 11 : 101 is a Prime number.