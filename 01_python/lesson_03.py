num1 = int(input("Enter number: "))
hasBobCar = False

if num1 > 50 and not hasBobCar:
    print("More then 50")

    text = input("Enter word: ")
    if text == "Word":
        print("Word")
elif 5 < num1 < 10 or hasBobCar:
    print("Good")
elif num1 == 11:
    print("Number is 11")
elif num1 == 12:
    print("Number is 12")
else: 
    print("Else")

number = float(input("Enter number: "))
result = "More then 5.5" if number > 5.5 else "Less then 5.5"
# if number > 5.5:
#     result = "More then 5.5"
# else: 
#     result = "Less then 5.5"
print(result)