# Problem statement: Print prime factors of n:
# input provided by user: n
# output: prime factors of n

# take input from user:
n = int(input("Enter a number: "))
print()

# Approach #1: BF(Brute Force):
def primeFact_BF(num):
    fact = [] 
    expo = []
    i=0
    d=2
    while(num>1):
        k=0
        while(num%d==0):
            num/=d
            k+=1
        if(k>0):
            fact.append(d)
            expo.append(k)
            i+=1
        d+=1
    
    print(f"BF: Prime factors of {n}:")

    # without list comprehension:
    # ---------------------------
    # for i in range(len(fact)):
    #     print(str(fact[i]) + "^" + str(expo[i]))
    
    # with list comprehension:
    # ------------------------
    print([str(fact[i]) + "^" + str(expo[i]) for i in range(len(fact))])


###################################################################################################


# Approach #2: BA(Better Approach) : minimize how many times the first while loop runs:
    # we add an additional check in first while loop to check d*d <= num so that
    # when our num is a prime number or has been reduced to a prime number(due to n/=d) 
    # then in that case we don't need to run the while loop further but just add that 
    # num to our fact list which will minimize the number of times our while loop runs.
def primeFact_BA(num):
    fact = [] 
    expo = []
    i=0
    d=2
    while(num>1 and d*d <= num):
        k=0
        while(num%d==0):
            num/=d
            k+=1
        if(k>0):
            fact.append(d)
            expo.append(k)
            i+=1
        d+=1
    if(num>1):
        fact.append(int(num))
        expo.append(1)

    print(f"BA: Prime factors of {n}:")

    # without list comprehension:
    # ---------------------------
    # for i in range(len(fact)):
    #     print(str(fact[i]) + "^" + str(expo[i]))
    
    # with list comprehension:
    # ------------------------
    print([str(fact[i]) + "^" + str(expo[i]) for i in range(len(fact))])

# Brute-Force:
primeFact_BF(n)
print()
# Better-Approach:
primeFact_BA(n)
print()

# OUTPUT:
# =======
# Enter a number: 5105100

# BF: Prime factors of 5105100:
# ['2^2', '3^1', '5^2', '7^1', '11^1', '13^1', '17^1']

# BA: Prime factors of 5105100:
# ['2^2', '3^1', '5^2', '7^1', '11^1', '13^1', '17^1']

