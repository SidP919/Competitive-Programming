t = (1, 2, 3)
#tuples are immutable or unchangeable i.e. we cannot make changes into it.

credit_card1 = (115165156161, 'Joe Rogan', '11/20', 123)
credit_card2 = (561566566565, 'Joeaskhf Rogaadsdfn', '11/20', 123)

credit_cards = [credit_card1, credit_card2]

print(credit_cards)

#unpacking the tuple
person = ("Nancy-pants", 25, "Pizza")
(name, age, favFood) = person
print(name)
print(age)
print(favFood)

person1 = ("sid", 25, "Pizza")
person2 = ("pandey", 25, "Pasta")
people = [person1, person2]
for name, age, favFood in people:
  print()
  print(name)
  print(age)
  print(favFood)

# OUTPUT:
# =======
# [(115165156161, 'Joe Rogan', '11/20', 123), (561566566565, 'Joeaskhf Rogaadsdfn', '11/20', 123)]
# Nancy-pants
# 25
# Pizza

# sid
# 25
# Pizza

# pandey
# 25
# Pasta