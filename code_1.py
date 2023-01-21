import random
import time

a=int(random.randrange(0,90,10))
b=a+10
n=random.randint(a,b) # Generating Random Number between 0 to 100

def clue1(n): # Finding the First Number
    n1=int(n)
    while(n1>0):
        tmp=n1%10
        n1=int(n1/10)
    return tmp


def clue2(n): # Finding Multiples of N
    l=[]
    for i in range(1,9):
        if(n%i)==0:
            l.append(i)
    return l

def countdown(t): # Printing Countdown
    
    while t:
        timer = '{:02d}'.format(t) # Formatting to display in 2 digits 
        print("Reveling the Next Clue in: "+timer,end='\r')
        time.sleep(1)
        t -= 1
    print()

print("Guess the Random Number between "+a+" and "+b)

nin=int(input())
if (n==nin):
    print("Congrats")
else:
    print("Second Clue : The Nuber starting with ",clue1(n))



