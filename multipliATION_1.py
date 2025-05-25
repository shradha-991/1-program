# n=int(input("Enter no:"))
# s=0
# s1=0
# s2=0
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)
#     s+=n*i
#     s1+=i
#     s2+=n
# print("_________________________________")
# print(s2,"*",s1,"=",s)
n=int(input("Enter no:"))
i=1
s=0
s1=0
s2=0
while(i<=10):
    print(n,"*",i,"=",n*i)
    i=i+1
    s+=n*i
    s1+=i
    s2+=n
print("_________________________________")
print(s2,"*",s1,"=",s)