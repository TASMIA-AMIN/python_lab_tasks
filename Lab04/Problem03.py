def checkPal(x):
    rev = ""
    for a in reversed(st):
        rev += a

    if(x == rev):
        print("Pallindrome")
    else:
        print("Not a Pallindrome")

st = input("Enter a string: ")
checkPal(st)


