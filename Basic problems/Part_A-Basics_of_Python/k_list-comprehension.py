names = ["Jennifer", "Susan", "Jane", "Sophie"]
l = []

# List Comprehension:
# ===================

# Example #1:
# -----------
for person in names:
  l.append(person)
print(l)
# now with list comprehension:
print([person for person in names])
print()

# OUTPUT: 
# ['Jennifer', 'Susan', 'Jane', 'Sophie']
# ['Jennifer', 'Susan', 'Jane', 'Sophie']


l=[]
# Example #2:
# -----------
for person in names:
  l.append(person + ' dumped me.')
print(l)
# now, with list comprehension:
print([person + " dumped me." for person in names])
print()

# OUTPUT:
# ['Jennifer dumped me.', 'Susan dumped me.', 'Jane dumped me.', 'Sophie dumped me.']
# ['Jennifer dumped me.', 'Susan dumped me.', 'Jane dumped me.', 'Sophie dumped me.']


l = []
# Example #3:
# -----------
movies_and_ratings = {"3 Idiots":9.5, "Sholay":8.5, "Swades":8, "Raone":7}
print(movies_and_ratings)

for movie in movies_and_ratings:
  if movies_and_ratings[movie]>8:
    l.append(movie)
print(l)
# now, with List Comprehension:
print([movie for movie in movies_and_ratings if movies_and_ratings[movie]>8])

# OUTPUT:
# {'3 Idiots': 9.5, 'Sholay': 8.5, 'Swades': 8, 'Raone': 7}
# ['3 Idiots', 'Sholay']
# ['3 Idiots', 'Sholay']
