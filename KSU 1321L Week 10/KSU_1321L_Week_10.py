# Class : CSE 1321L
# Section : B09
# Term : Fall 2026
# Instructor : Jui Mhatre
# Name : Dominic Lyu
# Lab : 9A

from email.mime import application


emailList = []

while True:
    print("[Mailing List]\n")

    print("1 - Add email\n2 - Delete email\n3 - List all email\n4 - Quit")
    inA = input("Make your selection: ")

    if inA == "1":
        emailAdd = input("Enter the email to be added: ")
        emailList.append(emailAdd)
        print("Email added to mailing list.")

    if inA == "2":
        emailRemove = input("Enter the email to be removed: ")
        if emailRemove in emailList:
            emailList.remove(emailRemove)
            print(emailRemove + " has been removed from the mailing list.")
        else:
            print("No such email in mailing list: " + emailRemove)

    if inA == "3":
        for i in range(len(emailList)):
            print(emailList[i])

    if inA == "4":
        print("\nShutting down...")
        break()