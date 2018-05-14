import time
subjects = ['English','Math','Science','Spanish','History']
for i in subjects:
    if i == "English":
        print("My favorite subject is " + i)
    else:
        print("I also take " + i)
friends = ['alexa','georgia','sofia','margot','lauren']
for i in friends:
    print(i.title() + " is awesome!")
    
myname = ""
letters = ['r','o','r','y',' ','a','s','h','m','e','a','d','e']
for i in letters:
    myname = myname + i
    print(myname)
    time.sleep(0.5)
    
