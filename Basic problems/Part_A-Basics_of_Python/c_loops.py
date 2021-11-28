# Loops in Python:
# ================

n = 10

# Now, let's find the sum of first n natural numbers.

# While loop:
# ============
i = 1
sum = 0
while i <= n :
    sum = sum + i
    i+=1
print("While Loop: Sum of first " + str(n) + " natural numbers is " + str(sum))

# For loop:
# =========
i = 1
sum = 0
for i in range(n+1):
    sum = sum + i
    i+=1
print("For Loop: Sum of first " + str(n) + " natural numbers is " + str(sum))

# NOTE: Please do see Part_B/a_sum_of_first_n_numbers.py 
# to know a better solution to this problem of finding 
# sum of first n natural numbers.
