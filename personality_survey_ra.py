while True:
    print("What's your favorite sport?")
    sport = input()

    if sport == "basketball":
        print("Wow, basketball is my favorite sport too!")
    elif sport == "sailing":
        print("I'm not great at sailing, maybe you could teach me.")
    elif sport == "dance":
        print("I can't dance.")
    else:
        print("I  don't play " + sport)
    print("What's your favorite TV show?")
    tvshow = input().title()

    if tvshow == "The Cosby Show":
        print("That's the stupidest thing I've ever heard!")
    elif tvshow == "Matlock":
        print("I love murder mysteries.")
    else:
        print(tvshow + " sounds funny.")
        
    print("What's your favorite book?")
    book = input()
    if book == "Chronicles of Narnia":
          print("C.S. Lewis is a genius!")
    else:
        print("Cool.")
    print("What's is your favorite subject?")
    subject = input()
    if subject == "math":
          print("What's the square root of 225")
          answer = input()
          if answer == "15":
              print("You're good.")
          else:
              print("You need to practice.")
    else:
        print(subject + " is hard for me.")
    print("Play again? (Yes/No)")
    answer = input()
    if answer == "Yes":
        print("Get ready!")
    else:
        print("See ya!")
        break
      
