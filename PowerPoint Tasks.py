import random

# High-Low

Number = random.randrange(0, 100)
print(Number)
UserGuess = 0
while UserGuess != Number:
    UserGuess = input("PLease enter a number and the computer will state higher or lower ")
    if UserGuess > str(Number):
        print("Lower")
    elif UserGuess < str(Number):
        print("Higher")
    else:
        print("Correct")
        break


#