#Program calculates as many values of the Fibonacci Succession as the user
#inputs when asked.

fib = []
a, b = 0, 1
inputIsNumber = False

#Ask for input and check if it is a number. Re-prompts the user if otherwise.

while not inputIsNumber:
    userInput = input("How many numbers of the Fibonacci Succession do you want"
    " to print? ")
    try:
        numInput = int(userInput)
        inputIsNumber = True
    except ValueError:
        print("Please make sure to enter a number.")

#Fibonacci algorithm.

while len(fib) < numInput:
    fib.append(a)
    a, b = b, a + b

print(fib)
