isUserInput = False
while not isUserInput:
    try:
        num = int(input("Enter num: "))
        isUserInput = True
        print(num)
    except ValueError:
        print("Must enter a number")