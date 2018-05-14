import random

words = ["cat","dog","bird","frog","flower"]
hint1 = ["tail","tail","beak","tongue","stem"]
hint2 = ["meow","bark","chirp","ribbit","petal"]
number = random.randint(0,4)
secretword = words[number]
guess = ""
counter = 0

while True:
    print("Guess the secret word!")
    print("Type 'hint1', 'hint2', 'length', 'first letter', 'last letter', or 'give up' if you need help.")
    guess = input()
    if guess == secretword:
        counter += 1
        print("You win!")
        print("It took you " + str(counter) + " guesses.")
        break
    elif guess == "hint1":
        print(hint1[number])

    elif guess == "hint2":
        print(hint2[number])

    elif guess == "length":
        print(len(secretword))

    elif guess == "first letter":
        print(secretword[0])

    elif guess == "last letter":
        print(secretword[-1])

    elif guess == "give up":
        print("The secret word was " + secretword)
        break
    else:
        print("Try again.")
        counter += 1
    
        
