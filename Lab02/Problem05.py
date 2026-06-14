num = int(input("Enter your marks: "))

if num>=90 and num<=100:
    print("A+")
elif num>=85 and num<90:
    print("A")
elif num>=80 and num<85:
    print("B+")  
elif num>=75 and num<80:
    print("B")
elif num>=70 and num<75:
    print("C+") 
elif num>=65 and num<70:
    print("C")
elif num>=60 and num<65:
    print("D+")
elif num>=50 and num<60:
    print("D")
elif num<50 and num>=0:
    print("F")
else:
    print("Not a valid number!!!")
