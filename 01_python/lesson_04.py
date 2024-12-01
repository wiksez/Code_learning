data = [5, 7.4, True, "Word", 56, [0, 15]]
data[2] = False
print(data[-1][1])

data.append('info')
new_list = [5, 7, 3]
data.extend(new_list)
data.insert(1, 0.567)
data.remove('info')
data.pop(0)
new_list.sort()
data.reverse()
# data.clear()
print(new_list)
print(data)
print(data.count(5))
print(len(data))

print(data[::3])

# Strings
word = list('Some')
word[0] = 'T'
print(word.count('m'))
print(len(word))

word2 = 'Hello'
print(word2.upper())
print(word2.find('l'))
