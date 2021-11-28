# Lists:
# =======

# Basic operations on lists in python:
# -------------------------------------
l = [1,3,2]

l2 = [1, 'ewer', "sdsfs",2, 3, [1, 2, 3]]

print(l + l2)

names = ["joe", "john", "james"]

print(names)

names.append("gary")
print(names)

names.insert(1, "Sid")
print(names)

# names.remove("Sid")
# print(names)

names.reverse()
print(names)


#################################################################################################
# Sorting of lists in python:
# ---------------------------
print("\nSorting of lists in python: \n")

numbers = [6, 4,3, 2 , 7]
print(numbers)
numbers.sort()
print("\nSorted Array:")
print(numbers)


##################################################################################################
print("\n")
# Looping through lists in python:
# --------------------------------
for i in numbers:
  print(i)

###################################################################################################

# OUTPUT:
# ========

# [1, 3, 2, 1, 'ewer', 'sdsfs', 2, 3, [1, 2, 3]]
# ['joe', 'john', 'james']
# ['joe', 'john', 'james', 'gary']       
# ['joe', 'Sid', 'john', 'james', 'gary']
# ['gary', 'james', 'john', 'Sid', 'joe']

# Sorting of lists in python:

# [6, 4, 3, 2, 7]

# Sorted Array:
# [2, 3, 4, 6, 7]

# 2
# 3
# 4
# 6
# 7