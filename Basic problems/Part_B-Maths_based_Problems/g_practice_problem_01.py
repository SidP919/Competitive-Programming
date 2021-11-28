# Problem Link: https://leetcode.com/problems/self-dividing-numbers/ 
# Solution code:
from typing import List

a = int(input("Enter starting value = "))
b = int(input("Enter ending value = "))
print()
def selfDividingNumbers(left: int, right: int) -> List[int]:
    list = []
    end = right + 1
    start = left
    for i in range(start, end):
        if(i<10):
            list.append(i)
        else:
            tempInp=i #tempInp = 128
            while(tempInp>0):   # true true true
                curDivisor=tempInp%10   # curDivisor = 8 , 2 , 1
                if curDivisor==0:
                    break
                elif i%curDivisor!=0:   # true true true
                    break
                else:
                    if tempInp!=curDivisor:    # true true 
                        tempInp=int(tempInp/10)   # tempInp = 12 , 1 ,
                    else:    # true
                        list.append(i)  # add i = 128 to list
                        break
    return list

print(f"Self-Dividing-Numbers from {a} to {b} : {selfDividingNumbers(a, b)}")          
                    
# OUTPUT:
# =======
# Enter starting value = 8
# Enter ending value = 29

# Self-Dividing-Numbers from 8 to 29 : [8, 9, 11, 12, 15, 22, 24]