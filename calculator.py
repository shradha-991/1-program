choice=input("choose any 1 opr+,-,*,/,%,**,//:")
x=int(input("Enter 1st num:"))
y=int(input("Enter 2nd num:"))
if choice=="+":
    res=x+y
    print(res)
elif choice=="-":
    res=x-y
    print(res)
elif choice=="*":
    res=x*y
    print(res)
elif choice=="/":
    res=x/y
    print(res)
elif choice=="%":
    res=x%y
    print(res)
elif choice=="**":
    res=x**y
    print(res)
elif choice=="//":
    res=x//y
    print(res)
else:
    print("invalid")