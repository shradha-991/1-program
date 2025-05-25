
print("____VOTING SYSTEM FOR THOSE WHO ELIGIBLE TO GIVE VOTE____")
name=input("Enter your name:")
Age=int(input("Enter your age:"))
if (Age>18):
    print("YOU ARE ELIGIBLE TO VOTE , VOTE PLEASE!!")
    print("Choose your vote:")
    print("1.BJP,2.Congress,3.Bhaujan Samaj Party")
    Choice=int(input("Enter your choosen vote1.,2.,3.:"))
    if Choice==1:
        print("BJP")
        print(" YourVote gives to Lotus ")
    elif Choice==2:
        print("Congress")
        print("Your vote gives to Hand")
    elif Choice==3:
        print("Bhaujan Samaj Party")
        print("Your Vote gives to Elephant")
   
    else:
        print("INVALID CHOICE")
else:
    print("YOU ARE NOT ELIGIBLE TO GIVE VOTE coz YOU ARE UNDERAGE")




