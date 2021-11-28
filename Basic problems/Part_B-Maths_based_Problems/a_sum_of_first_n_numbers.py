# Problem statement: Find the sum of first n natural numbers
# input provided by user: n
# output: value of 1 + 2 + 3 + ... + n

# take input from user:
n = int(input("Enter a number: "))
print()

# Approach #1: BF(Brute Force):
sum = 0
for i in range(n+1):
    sum = sum + i
print(f"BF: with for loop, result = {sum}")
print()

# Approach #2: BA(Better Approach): Gauss's sum:
sum2 = (n*(n+1))/2
print(f"BA: with Gauss's sum, result = {sum2}")
print()

# OUTPUT:
# =======
# Enter a number: 50

# BF: result = 1275

# BA: with Gauss's sum, result = 1275.0