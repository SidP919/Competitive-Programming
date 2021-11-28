digits = [0,1,2,3,4,5,6,7,8,9]
print(f"Digits Array: {digits}")

# OUTPUT:
# =======
# Digits Array: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Striding of Lists:
# ==================
print(digits[0:10: 2]) # print array by skipping (2-1) element in between.

print(digits[::2]) # print array by skipping (2-1) element in between.

print(digits[::-2]) # print reverse of array starting with last element by skipping (2-1) elements in between.

print(digits[::-1]) # print reverse of array starting with last element by skipping (1-1) elements in between.

print(digits[5:0:-2]) # print reverse of array starting with digits[5] to digits[1] by skipping (2-1) elements in between.
print("\n")
# OUTPUT:
# =======
# [0, 2, 4, 6, 8]
# [0, 2, 4, 6, 8]
# [9, 7, 5, 3, 1]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# [5, 3, 1]

# Striding with range:
# ====================
for i in range(3, 16, 3):           #16 excluded
    quotient = i / 3
    print(f"{i} divided by 3 is {int(quotient)}.")
print('\n')

for i in range(15, 2, -3):          #2 excluded
    quotient = i / 3
    print(f"{i} divided by 3 is {int(quotient)}.")
print('\n')

# OUTPUT:
# =======
# 3 divided by 3 is 1.
# 6 divided by 3 is 2.
# 9 divided by 3 is 3.
# 12 divided by 3 is 4.
# 15 divided by 3 is 5.

# 15 divided by 3 is 5.
# 12 divided by 3 is 4.
# 9 divided by 3 is 3.
# 6 divided by 3 is 2.
# 3 divided by 3 is 1.