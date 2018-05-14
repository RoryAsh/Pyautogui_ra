#Interview Function
def question(question):
    global answer
    answer = input(question)
    print(answer)
#Interview Questions
question("What's your name?  ")

question("What's your favorite class?  ")
if answer == "Math":
    question("Wonderful, what are you learning now?  ")
    print("Wow, I can almost remember studying " + answer + " when I was your age.")

question("Do you play any sports?  ")

question("What have you read recently?  ")
