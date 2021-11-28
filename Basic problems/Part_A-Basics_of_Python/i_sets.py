s = {'blueberry', 'rasberry'}

s.add('redberry')
print(s)

s.add("blueberry")
print(s)
# Sets always have unique elements only

#################################################################################################

# Casting of list to Set:
# -----------------------
l = [1, 2, 3, 3, 4, 4, 4, 5, 'abc', 'abc']
no_duplicate_set = set(l)
print(no_duplicate_set)

#################################################################################################

# Operations on Sets:
# -------------------
library1 = {'Harry Potter', "Hunger Games", "Lord of Rings"}
library2 = {'Harry Potter', 'Romeo & Juliet'}

#union:
all_the_books = library1.union(library2)
print(all_the_books)

#intersection:
at_both_libraries = library1.intersection(library2)
print(at_both_libraries)

#difference:
not_at_lib2_but_at_lib1 = library1.difference(library2)
print(not_at_lib2_but_at_lib1)

#symmetric difference: extracts the common ones of the 2 lists.
sym_diff = library1.symmetric_difference(library2)
print(sym_diff)

#clear:
library1.clear()
print(library1)

################################################################################################

# OUTPUT:
# =======
# {'blueberry', 'redberry', 'rasberry'}
# {'blueberry', 'redberry', 'rasberry'}
# {1, 2, 3, 4, 5, 'abc'}
# {'Romeo & Juliet', 'Lord of Rings', 'Harry Potter', 'Hunger Games'}
# {'Harry Potter'}
# {'Lord of Rings', 'Hunger Games'}
# {'Lord of Rings', 'Romeo & Juliet', 'Hunger Games'}
# set()
