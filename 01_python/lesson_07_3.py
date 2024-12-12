try:
    num = int(input("Enter num: "))
    # f = open(f'data/file{num}.txt', 'r')
    # print(f.read())
    # f.close()

    with open(f'data/file{num}.txt', 'r', encoding='utf-8') as f:
        print(f.read())
        
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("You must enter number")
finally:
    print("Finish")