import random
number=[]
attempts=0
def makenumber():
    for i in range(3):
        x=random.randrange(0,9)
        number.append(x)
    if len(number)>len(set(number)):
        number.clear()
        makenumber()
def playgame():
    global attempts
    attempts+=1
    cows=0
    bulls=0
    print(number)
    choice=input("please enter a 3 digit number")
    guess=[]
    for i in range(3):
        guess.append(int(choice[i]))
    for i in range(3):
        for j in range(3):
            if (guess[i]==number[j]):
                cows+=1
    for x in range(3):
        if (guess[x]==number[x]):
            bulls+=1
    print("bulls:",bulls)
    print("cows:",cows)
    if (bulls==3):
        print("you won after",attempts,"attempts!")
    if (bulls!=3):
        playgame()
makenumber()
playgame()