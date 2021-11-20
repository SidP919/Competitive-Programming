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
print(f"with BF: sum = {sum}")
print()

# Approach #2: Gauss's sum:
sum2 = (n*(n+1))/2
print(f"with Gauss's sum: {sum2}")
print()
