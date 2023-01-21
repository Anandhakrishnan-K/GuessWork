import random
import time

def clue1(n): # Finding the First Number
    n1=int(n)
    while(n1>0):
        tmp=n1%10
        n1=int(n1/10)
    return tmp


def clue(n): # Finding Multiples of N
    l=[]
    for i in range(2,int(n/2)):
        if(n%i)==0:
            l.append(i)
    if(len(l)==0):
        print("and its a prime Number and the Number starting with",clue1(n))
    else:
        print("and the Number is a Multiples of: ",l)

def countdown(t): # Printing Countdown
    
    while t:
        timer = '{:02d}'.format(t) # Formatting to display in 2 digits 
        print("Reveling Number in: "+timer,end='\r')
        time.sleep(1)
        t -= 1
    print("The Number you missed to Guess is: ",n)




onemore='y'
while (onemore.upper()!='N'):
    a=int(random.randrange(0,80,10))
    b=a+20
    n=random.randint(a,b) # Generating Random Number between 0 to 100

    print("There is one Random Number generated between ",a," and ",b)
    clue(n)
    score=100
    nin=int(input("Guess the Random Number: ")) # Receiving the First Guess
    if (n==nin):
        print("Congrats you have found the correct Number")
        print("You Got ",score," Percentage !!!!")
    else:
        score-=20
        giveup=input(("That is not a correct Number, Want to GiveUp ? (y/n):"))
        if giveup.lower()=='n':
            print("One more clue for you, the Number ending with: ",n%10)
        while(giveup.lower()!='y' and score > 0):
            nin=int(input("Guess the Random Number: ")) # Receiving the following guesses
            if (n==nin):
                print("Congrats you have found the correct Number")
                print("You Got ",score," Percentage !!!!")
                break
            else:
                score-=40
                giveup=input(("That is not a correct Number, Want to GiveUp ? (y/n):"))
        if (giveup=='y' or score == 0):
            countdown(10)
    onemore=input("Want to try one more ? (y/n): ")
        


