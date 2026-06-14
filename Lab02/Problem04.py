x = input("Enter a character: ").lower()
if len(x)>1:
    print("Not a character!!!")
else:
   if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
       print("vowel")
   elif x=='b' or x=='c' or x=='d' or x=='f' or x=='g' or x=='h' or x=='j' or x=='k' or x=='l' or x=='m' or x=='n' or x=='p' or x=='q' or x=='r' or x=='s' or x=='t' or x=='v' or x=='w' or x=='x' or x=='y' or x=='z':
       print("consonant")
   else:
       print("Not a character!!!")