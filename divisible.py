n=int(input("Enter the number"))
if (n%3==0 and n%7==0):
    print("n is divisible by both 3 and 7.")
elif (n%3==0):
     print("n is divisible by 3.")
elif (n%7==0):
    print( "n is divisible by 7.")
else:
    print( "n is not divisible by 3 or 7.")