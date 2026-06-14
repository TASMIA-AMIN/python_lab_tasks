bas = int(input("Enter the base number: "))
pow = int(input("Enter the power value: "))

result = 1

for x in range(pow):
    result *= bas
else:
    print("Exponetiation is:", result)