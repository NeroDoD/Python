from random import randint

#Get the number of sides of the 'dice'
while True:
    diceSides = input("How many sides does the dice have?: ")
    try:
        diceSides = int(diceSides)
        break
    except ValueError:
        print("Please enter a number.")
#Get the number of 'rolls' the program must execute
while True:
    rollNumber = input("How many times should the dice be rolled?: ")
    try:
        rollNumber = int(rollNumber)
        break
    except ValueError:
        print("Please enter a number.")


#Start of the dice algorithm:
#Variable declaration
rollResult = []
i = 1
x = 1
#Roll dice 'rollNumber' times and append results to the 'rollResult' list
while i <= rollNumber:
    rollResult.append(randint(1, diceSides))
    i = i + 1

#Print how many times each possible number appeared
print(f"The dice had {diceSides} sides and was rolled {rollNumber} times.")
while x <= diceSides:
    if rollResult.count(x) == 0:
        print(f"The number {x} didn't appear.")
    elif rollResult.count(x) == 1:
        print(f"The number {x} appeared once.")
    else:
        print(f"The number {x} appeared {rollResult.count(x)} times.")
    x = x + 1

#OPTIONAL print all numbers from the aforementioned 'rollResult' list
while True:
    showResults = input("Do you want to view all the rolled numbers? Y / N: ")
    if (showResults == "Y") or (showResults == "y"):
        print(rollResult)
        break
    elif (showResults == "N") or (showResults == "n"):
        break
    else:
        print("Please answer Y or N for yes or no.")
