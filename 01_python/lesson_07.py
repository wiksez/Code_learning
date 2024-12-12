# user = input("Enter data: ")

# f = open('data/file.txt', 'a')
# f.write(user + "\n")
# f.close()

f = open('data/file.txt', 'r')
# print(f.read(10))
for line in f:
    print(line, end="")
f.close()