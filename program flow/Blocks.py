name = input("Please enter your name: ")
age = int(input("how old are you, {}?".format(name)))
print(age)

#if age >= 18:
#    print("You are old enough to vote")
#    print("Please put an X in the box")
#else:
#    print("plesae come back in {0} years".format(18 - age))

if age < 18:
    print("plesae come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry, Yoda, you die in return of the jedi")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")
