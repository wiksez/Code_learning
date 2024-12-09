lis = [1, 34, 8, 0, -5, 7, 32, 74, 59, 92, 41, 10, -2]
min_element = lis[0]
for el in lis:
    if min_element > el:
        min_element = el

lis.remove(min_element)
if min_element < 0:
    lis.append(min_element)
else:
    lis.insert(0, min_element)
print("Min element:", min_element)
print("New list:", lis)