data = (5, 4, 6, True, [6, 8])
# data[2] = 56
# data.count()
# print(data[::-3])
# print(len(data))
word = tuple('Some')

data2 = {5, 6, 8, 5}
data2.add(78)
data2.remove(6)
data2.clear()
word2 = frozenset('Hello')
# print(word2)

user = {'name': 'Alex', 'age': 15, 5: 6, True: 5}
user[(5,6)] = 6
user.popitem()
user.pop('age')
# print(user)

users = {
    'user1': {'name': 'Alex', 'age': 23, 'data': [5, 6, 3, 3], 'bio': 'Some text', 'adress': {'city': 'New York', 'street': ''}},
    'user2': {'name': 'Bob', 'age': 24, 'data': [5, 6, 3, 3], 'bio': 'Some text', 'adress': {'city': 'New York', 'street': ''}},
    'user3': {'name': 'Max', 'age': 21, 'data': [5, 6, 3, 3], 'bio': 'Some text', 'adress': {'city': 'New York', 'street': ''}},
    'user4': {'name': 'John', 'age': 23, 'data': [5, 6, 3, 3], 'bio': 'Some text', 'adress': {'city': 'New York', 'street': ''}},
}

print(users['user3']['name'])
print(users['user3']['adress']['city'])