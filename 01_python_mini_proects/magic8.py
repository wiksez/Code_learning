import random
name = "Andrew"
question = "Should I call Tom?"
answer = ""
random_number = random.randint(1, 11)
if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
elif random_number == 10:
    answer = "Signs point to yes"
elif random_number == 11:
    answer = "Cannot predict now"
else:
    answer = "Error"

if name != "" and question != "":
    print(name, "asks:", question)
    print("Magic 8-Ball's answer:", answer)
elif question == "":
    print("Ask your question")
else:
    print("Question:", question)
    print("Magic 8-Ball's answer:", answer)