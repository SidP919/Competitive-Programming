# Sieve of eratosthenes
# ======================

# Problem statement: find all the prime numbers less than or equal to n:
# input provided by user: n
# output: print prime numbers less than or equal to n

# take input from user:
n = int(input("Enter a number: "))
print()

# See below function which provides a way to solve this problem:
def printPrimeNumbers(n):
    primeNumList = [True]*(n+1) # this creates a list of length (n+1) with all its elements = True
    primeNumList[0] = False # 0 is not a Prime number
    primeNumList[1] = False # 1 is not a Prime number
    length = int(n/2)
    for i in range(2,length):  # len=n/2 bcoz j=2*i so, we only traverse till n/2 becoz at n/2, j = n
        if primeNumList[i]==True:
            for j in range(2*i,n+1,i):  # Striding: loop from j=2*i to j=n while skipping i elements in between.
                primeNumList[j]=False   # multiple of a primeNumber is not a primeNumber(ex. 4, 6, 8... are multiples of 2)
    print([ind for ind in range(len(primeNumList)) if primeNumList[ind]==True]) # print primeNumbers with list comprehension

printPrimeNumbers(n)