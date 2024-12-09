user_data = []
number =  int(input("Enter number: "))
for i in range(number):
    el = int(input("Enter value: "))

    user_data.append(el)

print(user_data)

maxElement = 0
for i in user_data:
    if i > maxElement:
        maxElement = i

print("Max element: ", maxElement)