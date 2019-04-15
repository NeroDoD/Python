def getMiddle(string):
    #Check whether the string has an even or odd number of characters.
    if len(string) % 2 == 0:
        #String is even.
        mid = int(len(string) / 2)
        return (f"You entered the word '{string}', which has an even "
        f"number of characters. The two middle ones are '{string[mid-1]}' and "
        f"'{string[mid]}'.")
    else:
        #String is odd.
        mid = int((len(string) -1) / 2)
        return (f"You entered the word '{string}', which has an odd "
        f"number of characters. The middle one is '{string[mid]}'.")

#Ask user for input.
word = input("Enter a word: ")
print(getMiddle(word))
