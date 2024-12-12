try:
    message = "Hello"
    f = open('data/example.txt', 'x')
    f.write(message)
    f.close()
except FileExistsError:
    f = open('data/example.txt', 'a')
    message = "\n" + input("Add something: ")
    f.write(message)
    f.close()
    print("You have this file. You can add something")