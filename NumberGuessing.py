import random 
import math
lower = int(input("Enter lower limit..."))
upper = int(input("Enter upper limit..."))

x = random.randint(lower,upper)

chances = round(math.log(upper-lower+1,2))
print("You have only",chances," changes to guess the number")
 
count = 0
while count < chances:
    count= count+1 
    guess = int(input("Guess a number in the given range"))
    if x==guess:
        print("You have guessed it right")
        break
    elif guess<x:
        print("You have guessed it low")
    else:
        print("You have guessed it high")
if count>chances:
    print("The number is %d"%x)
    print('Better luch next time!!!')