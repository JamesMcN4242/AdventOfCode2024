import os.path

while True:
    print("What solution do you want to run?\nNon-int number to exit.")
    strInput = input()

    if strInput.isnumeric() == False:
        break

    dayNum = int(strInput)
    if dayNum < 1 or dayNum > 25:
        print("Invalid day number.\n\n\n")
    elif os.path.isfile(f"solutions/day{dayNum}.py") == False:
        print("File not found. Perhaps this day hasn't been completed yet.\n\n\n")
    else:
        exec(open(f"solutions/day{dayNum}.py").read())
        print("\n\n\n")