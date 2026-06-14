max = int(input("Enter the maximum number: "))
num1 = 0
num2 = 1
print("Fibonacci Series: ")
for x in range(max):
    if num1 > max:
        break
    else:
        print(num1)
        temp = num1
        num1 = num2
        num2 += temp


