#Print X asterisks per line and then print X-1 asterisks in the following
#lines until X = 0. (Where X is a number that the user inputs)

symbol = input("What do you want the program to write?"
" (Default is asterisk): ")
if symbol == "": symbol = "*"

#Ask for input and check if it is a number. Re-prompts the user if otherwise.

checkForInputCompleted = False
while not checkForInputCompleted:
    userInput = input("Enter a number: ")
    try:
        userInput = int(userInput)
        checkForInputCompleted = True
    except ValueError:
        print("You didn't enter a number.")

#Symbol printer.

while userInput > 0:
    print(symbol * userInput)
    userInput -= 1
