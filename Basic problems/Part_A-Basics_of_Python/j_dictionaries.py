# import "OrderedDict" datatype from Package "collections",
# though after python 3.7 onwards dictionaries are by Default OrderedDict 
# i.e. they maintain the order of the elements in which they were added to the list i.e. we don't need to import anything, if we are working with Python 3.7 or above.
from collections import OrderedDict 

groceries = {'bananas':5, "oranges":3}
print(groceries.get("hello"))
print(groceries.get("bananas"))

groceries.__setitem__('bananas',2)#not recommended, use update
print(groceries.get("bananas"))

# OUTPUT:
# =======
# None
# 5
# 2

###########################################################################################################

# Dictionary inside a Dictionary:
contacts = {
  'Joe': {
    'phone': '1213132', 'email':'afff@g.com'
    },
  'jane':{
    'phone': '1213132', 'email':'afff@g.com'
  }
}
print(contacts.get('jane'))
print(contacts.get('jane').get('email'))

# OUTPUT:
# =======
# {'phone': '1213132', 'email': 'afff@g.com'}
# afff@g.com

############################################################################################################

# if u want to initiate an empty dictionary: 
# ------------------------------------------
w = dict.fromkeys([])
print("current dict w: " + str(w))
w.update({"sda":2, "sadf": 4})
print("after update, dict w: " + str(w))
print()

# OUTPUT:
# =======
# current dict w: {}
# after update, dict w: {'sda': 2, 'sadf': 4}

# Basic operations on a dictionary:
# ---------------------------------
#list the items:
print("items of dictionary: ")
print(w.items())
print(list(w.items()))
print()

# OUTPUT:
# =======
# items of dictionary:
# dict_items([('sda', 2), ('sadf', 4)])
# [('sda', 2), ('sadf', 4)]

#list the keys:
print("keys of dictionary: ")
print(w.keys())
print(list(w.keys()))
print()

# OUTPUT:
# =======
# keys of dictionary:
# dict_keys(['sda', 'sadf'])
# ['sda', 'sadf']


#list the values:
print("values of dictionary: ")
print(w.values())
print(list(w.values()))
print()

# OUTPUT:
# =======
# values of dictionary:
# dict_values([2, 4])
# [2, 4]

#pop the particular item
print("popped: "+str(w.pop("sda")))
print("after poping particular item: "+str(w))
print()

# OUTPUT:
# =======
# popped: 2
# after poping particular item: {'sadf': 4}

#pop the upper most item
print("popped: "+str(w.popitem()))
print("after poping the upper most item: "+str(w))
print()

# OUTPUT:
# =======
# popped: ('sadf', 4)
# after poping the upper most item: {}

print(w.clear())

# OUTPUT:
# =======
# None

############################################################################################################

# Extra: Write a program to create a Dictionary which will contain all the words of below sentence as keys
# and their values will be equal to the number of times that word appears in the sentence.
sentence = "I like the name Sidharth bcoz the name Sidharth is the best :) or is it not ? :("

word_list = sentence.split(" ")
# word_list = ['I', 'like', 'the', 'name', 'Sidharth', 'bcoz', 'the', 'name', 'Sidharth', 'is', 'the', 'best']

# initializing word_count Dictionary:
word_count = {word_list[0]:0}
# word_count = {'I': 0}
print()

# Now, Add all the words of word_list to word_count dictionary and count their number of occurences.
for i in range(len(word_list)):
  
  count_of_a_word = word_count.get(word_list[i])
  
  if(word_count.get(word_list[i])==None):
    word_count.update({word_list[i]:1})
  else:
    word_count.update({word_list[i]:count_of_a_word+1})

print("Updated Dictionary: " + str(word_count))
print()

# OUTPUT:
# =======
# Updated Dictionary: {'I': 1, 'like': 1, 'the': 3, 'name': 2, 'Sidharth': 2, 
#   'bcoz': 1, 'is': 2, 'best': 1, ':)': 1, 'or': 1, 'it': 1, 'not': 1, '?': 1, ':(': 1}

###############################################################################################################
