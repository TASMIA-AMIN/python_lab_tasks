#isPrime = True
sum = 0
for x in range(2,1001):
    isPrime = True
    for y in range(2,x):
        if x%y==0:
            isPrime = False
            break
    if isPrime:
        sum += x
else:
    print("Sum of the prime numbers between 0 to 1000 is:", sum)
    
