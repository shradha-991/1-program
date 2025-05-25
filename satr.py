n=int(input())
for i in range(0,n):
    spaces=n-i
    while (spaces>0):
        print(" ",end=" ")
        spaces-=1
    for j in range(1,2*i):
        print("*",end=" ")
    print()        
for i in range(0,n):
    spaces=n-i
    while (spaces>0):
        print(" ",end=" ")
        spaces-=1
    for j in range(1,2*(n-i)):
        print("*",end=" ")
    print()