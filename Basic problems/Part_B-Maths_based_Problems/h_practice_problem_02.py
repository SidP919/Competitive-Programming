# Problem Link: https://leetcode.com/problems/powx-n/ 
# Solution code:

x = int(input("Enter value of x = "))
n = int(input("Enter value of n = "))
print()

def myPow(x: float, n: int) -> float:
    res = 1.0000
    if n < 0:
        posOrNeg = -1
    else:
        posOrNeg = 1
    n = abs(n)
    while n>=1:
        if n%2==0:
            x = x*x
            n/=2
        else:
            n-=1
            res*=x
    return res**posOrNeg

print(f"{x}^{n} = {myPow(x,n)}")

# OUTPUT:
# =======
# Enter value of x = 13
# Enter value of n = 5
#
# 13^5 = 371293.0

# Enter value of x = 13
# Enter value of n = -5
#
# 13^-5 = 2.693290743429044e-06

# Enter value of x = 0
# Enter value of n = 0
#
# 0^0 = 1.0
