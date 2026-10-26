# Class : CSE 1321L
# Section : B09
# Term : Fall 2026
# Instructor : Jui Mhatre
# Name : Dominic Lyu
# Lab : 9B

friendsList = []
ageList = []

print("[Friend List]")

while True:

    print("1 - Add friend\n2 - List friends\n3 - Quit")
    selection = input("Make your selection: ")

    if selection == "1":
        frName = input("\nEnter your friend's name: ")
        frAge = int(input("\nEnter your friend's age: "))
        friendsList.append(frName)
        ageList.append(frAge)
        print("\nFriend added")

    if selection == "2":
        for i in range(len(friendsList)):
            print("\nName: " + friendsList[i] + ", Age: " + str(ageList[i]))

    if selection == "3":
        print("\nShutting down...")
        break