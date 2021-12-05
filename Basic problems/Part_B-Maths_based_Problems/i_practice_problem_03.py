# Problem Link: https://leetcode.com/problems/count-primes/ 
# Solution code:

# Take input from user:
print()
n = int(input("Enter value of n = "))
print()

# function to return count of primes less than n:
def countPrimes(n: int) -> int:
    if(n<3):
        return 0
    result = n - 2
    primeNumbers = [True]*n
    for i in range(2,int(n/2)+1):
        if primeNumbers[i]:
            for j in range(i*2,n,i):
                if(primeNumbers[j]):
                    primeNumbers[j] = False
                    result-=1
    return result

# print result:
print(f"There are total {countPrimes(n)} Prime numbers less than {n}.")
print()

# OUTPUT:
# =======
#
# Enter value of n = 55
#
# There are total 16 Prime numbers less than 55.
#

#
# Enter value of n = 3
#
# There are total 1 Prime numbers less than 3.
#