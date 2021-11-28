digits = [0,1,2,4,6,8,9,12,15,18]
print(f"Digits Array: {digits}")

# Indexing of Lists in python:
# ============================
print("\nIndexing:")
print(digits[-1])
print(digits[-len(digits)])

# OUTPUT:
# -------
# 18
# 0

##################################################################################################

# Slicing of Lists in python:
# ===========================
print("\nSlicing:")
print(digits[:3])

print(digits[0: 8]) # notice that digits[8] = 15 got excluded whereas digits[0] = 0 was included.

print(digits[0:-1]) # notice that digits[-1] = 18 was excluded.

# OUTPUT:
# -------
# [0, 1, 2]
# [0, 1, 2, 4, 6, 8, 9, 12]
# [0, 1, 2, 4, 6, 8, 9, 12, 15]

##################################################################################################

# Loops and Slicing:
# ------------------
print("\nLoops with Slicing: ")
for i in range(len(digits)):
  print(digits[0:i])

print('\nPrinting 3 elements only at a time from digits array:\n')
window_length = 3
for i in range (len(digits)-(window_length-1)):
  print(digits[ i : i + window_length])

# OUTPUT:
# -------
# Loops with Slicing:
# []
# [0]
# [0, 1]
# [0, 1, 2]
# [0, 1, 2, 4]
# [0, 1, 2, 4, 6]
# [0, 1, 2, 4, 6, 8]
# [0, 1, 2, 4, 6, 8, 9]
# [0, 1, 2, 4, 6, 8, 9, 12]
# [0, 1, 2, 4, 6, 8, 9, 12, 15]

# Printing 3 elements only at a time from digits array:

# [0, 1, 2]
# [1, 2, 4]
# [2, 4, 6]
# [4, 6, 8]
# [6, 8, 9]
# [8, 9, 12]
# [9, 12, 15]
# [12, 15, 18]

############################################## END #################################################