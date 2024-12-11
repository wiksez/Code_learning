def test(word):
    print(word, "!", sep="")


def add(x=5, y=5, additional=0):
    res = x + y + additional
    test(res)

    return res

# add(5, 7)
# num1 = int(input("Enter num 1: "))
# num2 = int(input("Enter num 2: "))
# res = add(additional=15, y=7)
# print(res)

def mult(**kargs):
    for key, value in kargs.items():
        print(f"Element: {value}, key: {key}")

mult(x=6, y=8, additional=10, some="Word")