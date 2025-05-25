i=int(input("enter no:"))
orig=i
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if orig==sum:
    print("ARMSTRONG NO.:",orig)
else:
    print("NOT")