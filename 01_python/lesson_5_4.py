hobbies = 'skate, football, painting'
listHobbies = hobbies.split(', ')
newListHobbies = []

for i in listHobbies:
    newListHobbies.append(i.capitalize())

res = ", ".join(newListHobbies)
print(res)