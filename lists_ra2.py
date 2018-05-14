name = "Rory Ashmeade"

subjects = ["English", "Spanish", "Math", "History"]
print("My name is " + name)

for i in subjects:
    print("I take " + i + " as one of my classes.")


genres = ["soul", "jazz", "rock"]

for i in genres:
    if i == "soul":
        print("Soul music is so emotional.")
    elif i == "jazz":
        print("Jazz music is so syncopated.")
    elif i == "rock":
        print("Rock and roll is so fierce.")

books = []
while True:
    print("What is your favorite book? Type 'end' to stop program.")
    answer = input()
    if answer == "end":
        break
    else:
        books.append(answer)

for i in books:
    print(i + " is one of your favorites.")
    
