print("____VOTING SYSTEM FOR THOSE WHO ELIGIBLE TO GIVE VOTE____")
while True:
    name=input("Enter your name:")
    Age=int(input("Enter your age:"))
    if Age <= 18:
        print("YOU ARE NOT ELIGIBLE TO GIVE VOTE coz YOU ARE UNDERAGE")
        continue
    print("YOU ARE ELIGIBLE TO VOTE , VOTE PLEASE!!")
    print("Choose your vote:")
    print("1.BJP,2.Congress,3.Bhaujan Samaj Party")
    while True:
        Choice=int(input("Enter your choosen vote (1, 2, or 3):"))
        if Choice not in [1, 2, 3]:
            print("INVALID CHOICE. Please enter a valid option (1, 2, or 3).")
            continue
        if Choice==1:
            print("BJP")
            print(" YourVote gives to Lotus ")
        elif Choice==2:
            print("Congress")
            print("Your vote gives to Hand")
        elif Choice==3:
            print("Bhaujan Samaj Party")
            print("Your Vote gives to Elephant")
        break
    break