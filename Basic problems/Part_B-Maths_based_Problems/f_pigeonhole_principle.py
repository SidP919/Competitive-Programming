# Pigeonhole Principle:
# =====================
# If there are n+1 pigeons and n pigeonholes, 
# then atleast 1 pigeonhole will have more than 1 pigeon.
# Problem statement: Find a number with just 0s and/or 1s which is divisible by n:
# input provided by user: n
# output: the number with just 0s and/or 1s which is divisible by n

# take input from user:
n = int(input("Enter value of n: "))

# Solution code:
# ==============
def findDivisor(n):
    currentRem = 0  # initially, we assume our remainder is 0
    result = ""
    freqRem = [0]*(n+1) # freqRem = [0, 0, 0, ... , 0, 0] whose length is n+1
    for i in range(1,n+1):
        currentRem = ((currentRem*10 + 1) % n)  # current remainder
        
        if(currentRem == 0):    # if currentRem = 0 then we found the number which is divisible by n
            result=""
            for j in range(int(i)):    #  for ex.: 111 is divisible by 3
                result = result + "1"   # result = (number with i digits where all digits are 1)
            break
        elif freqRem[currentRem] != 0:  # means we have already got a number for which remainder was same.
            result=""
            OnesLength=int(freqRem[currentRem]+1)   # number of 1s in the result
            ZeroesLength=int(freqRem[currentRem])   # number of 0s in the result
            for k in range(1,OnesLength):
                result = result + "1"
            for k in range(ZeroesLength):
                result = result + "0"
            break
        
        else:   # this means we haven't encountered this current remainder yet
            freqRem[currentRem]=i   # we put current i in freqRem list, 
            # so we can use it later when we find the same remainder as currentRem for any other value of i
    print(f"{result} is the number consisting of only 0s and/or 1s that is divisible by {n}")   # print result
        
findDivisor(n)

# OUTPUT:
# =======
# Enter value of n: 47
# 1111111111111111111111111111111111111111111111 is the number consisting of only 0s and/or 1s that is divisible by 47
