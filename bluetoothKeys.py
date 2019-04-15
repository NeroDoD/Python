#Convert macOS bluetooth keys to Windows format.
#Example input (From macOS): 1df514b6 55934b00 1c49d77b 83c80788
#Example output (For Windows): 88 07 c8 83 7b d7 49 1c 00 4b 93 55 b6 14 f5 1d

while True:
    key = input("Enter a macOS formatted Bluetooth key: ")
    #Filters spaces out of the key.
    key = key.replace(" ", "")
    #Key must be 32 characters long without spaces.
    if len(key) == 32:
        keyList = []
        a, b = 30, 32
        while a >= 0:
            keyList.append(key[a:b])
            b = a
            a = a - 2

        winKey = "".join([str(x + " ") for x in keyList])
        linKey = "".join([str(x) for x in keyList])
        print(f"Your generated Windows key is: {winKey}")
        print(f"Your generated Linux key is: {linKey}")
        break
    else:
        print("Please enter a correctly formatted key.")
        print("E.g: 1df514b6 55934b00 1c49d77b 83c80788")
