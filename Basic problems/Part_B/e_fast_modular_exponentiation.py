# Fast Modular Exponentiation:
# ============================
# Problem statement: calculate (a^n) % MOD in a more efficient way:
# input provided by user: a n MOD
# output: prime factors of n

# take input from user:
a = int(input("To Calculate (a^n)%MOD\nEnter value of a: "))
n = int(input("Enter value of n: "))
MOD = 1000000007
print(f"MOD is equal to {MOD}\n")

# Approach #1: BF(Brute Force):
# =============================
print(f"BF: After Normal Modular Exponentiation, result = {(a**n)%MOD}") # Time Complexity: O(n)


# Approach #2: BA(Better Approach) in terms of time complexity using Divide & conquer:
# =====================================================================================
# 2.1: Recursive Implementaion: 
# TimeComplexity: O(log n) but this takes a load on stack memory when n is too large
# but it is recommended over iterative way when n is not too large.
def fastExpo(a,n,MOD):
    # base case or flow stopping case:
    if n == 0:
        return 1
    # recursive case 1: when n is even:
    elif n%2==0:
        return fastExpo((a*a%MOD),(n/2),MOD)
    # recursive case 2: when n is odd:
    else:
        return (a*fastExpo(a,n-1,MOD)) % MOD

# 2.2: Iterative Implementation: 
# TimeComplexity: O(log n) but this is better when n is too large.
def fastExpoIterative(a,n,MOD):
    result = 1
    while(n >= 1):
        if n%2==0:
            a = (a*a)%MOD
            n = n/2
        else:
            result = (a * result) % MOD
            n-=1
    return result

print(f"BA: After Fast Modular Exponentiation(recursively), result = {fastExpo(a,n,MOD)}") # Time Complexity: O(log n)
print(f"BA: After Fast Modular Exponentiation(iteratively), result = {fastExpoIterative(a,n,MOD)}") # Time Complexity: O(log n)

# OUTPUT:
# =======
# To Calculate (a^n)%MOD
# Enter value of a: 5
# Enter value of n: 13
# MOD is equal to 1000000007

# BF: After Normal Modular Exponentiation, result = 220703118
# BA: After Fast Modular Exponentiation(recursively), result = 220703118
# BA: After Fast Modular Exponentiation(iteratively), result = 220703118
