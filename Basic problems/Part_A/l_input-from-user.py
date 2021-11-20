# Working with dynamic input or taking input from a user:
# =======================================================

# Example #1: Sum of two numbers provided by user:
# ===========
a = int(input('Enter a no: '))
b = int(input('Enter one more no: '))
c = a + b
print(f"Sum of numbers: {c}")
print()

##########################################################################################################

# Example #2: Calculate an arithmetic expression provided by user:
# ===========
calculator = eval(input("Enter an expression to calculate(like 5+3*6) and press enter: "))
print(f"Answer: {calculator}")
print()
while True:
    print("Do you want to evaluate another expression? press Y for YES and any other button for NO.")
    answer=input()
    if answer == 'Y' or answer == 'y':
        calculator = eval(input("Enter an expression to calculate(like 5+3*6) and press enter: "))
        print(f"Answer: {calculator}")
        print()
    else:
        print("Ok then, see ya!!")
        break

# OUTPUT:
# =======
# Enter a no: 5 
# Enter one more no: 6
# Sum of numbers: 11

# Enter an expression to calculate(like 5+3*6) and press enter: 4+6+6
# Answer: 16

# Do you want to evaluate another expression? press Y for yes and any other button for no.
# 5
# Ok then, see ya!!

## for command line arguments:
# import sys
# p = int(sys.argv[1]) # bcoz argv[0] contains python script filename
# q = int(sys.argv[2])
# r = p + q
# print(r)

