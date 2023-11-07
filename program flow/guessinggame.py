answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("you got it first time")
else:
    if guess < answer:
        print ("please guess higher")
    else: # guess must be greater than answer
        print ("please guess lower")
        gues = int(input())
        if guess == answer:
            print("well done, you guessed it")
        else:
            print("sorry, you have not guessed correctly")

    

#if guess < answer:
#    print("please guess higher")
#    guess = int(input())
#    if guess == answer:
#        print("well done, you guessed it")
#    else:
#        Print("Sorry, you have not guessed correctly")
#elif guess > answer:
#    print("please guess lower")
#    guess = int(input())
#    if guess == answer:
#        print("well done, you guessed it")
#   else:
#        print("Sorry, you have not guessef correctly")
#else:
#    print("you got it first time")
