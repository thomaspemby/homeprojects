# Libaries

import time

import re
import random

# Variables

LoggedIn = False
InMenu = True

GUsername = None
GEmail = None

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


# Functions

def emailvalidation(email):
    if(re.fullmatch(regex, email)):
        return True
    else:
        return False


def SignUp():

    NewCredentials = []

    newusername = ""
    newusername = str(input("Hey there new user, what should we call you? "))
    while len(newusername) < 6:
        newusername = str(input("So, your username seems to be below 6 characters. What do you really want to be called? "))

    NewCredentials.append(newusername)
    time.sleep(0.5)

    ValidEmail = False
    print("The next point of call would be to ask for your email address.")
    NewEmail = str(input("Please enter the email address you wish to use on this account: "))
    validemailaddress = emailvalidation(NewEmail)

    if validemailaddress == True:
        validemailaddress = True
    else:
        validemailaddress = False

    while validemailaddress == False:
        NewEmail = str(input("Sorry, that email doesn't seem to be valid. Please enter a valid email: "))

        validemailaddress = emailvalidation(NewEmail)

        if validemailaddress == True:
            validemailaddress = True
        else:
            validemailaddress = False



    # verrifiedemailistheirs = False

    # while verrifiedemailistheirs == False:

       # secretcode = random.randint(000000,999999)



    NewCredentials.append(str(NewEmail))
    #print(str(NewCredentials))

    print("Now comes the serious stuff!")

    # Password system

    Passwordvalid = False
    password1 = None
    Password2 = None

    while Passwordvalid == False:
        Password1 = str(input("Please enter a new password for your account: "))
        Password2 = str(input("Please repeat that password: "))

        if Password1 == Password2:
            if len(Password1) < 6:
                print("Password must be at least 6 characters long!")
            else:
                print("Thank you for your information!")
                Passwordvalid = True

        else:
            print("Password's did not match! Please repeat this process.")

    print("\nPlease hold on while we check your data!")
    time.sleep(2)

    NewCredentials.append(Password1)

    # Check that the user wants to upload the data!

    UserChosen = False

    print("Are you sure that you would like to register with these details: ")
    for i in range(0, len(NewCredentials)):
        if i == 0:
            print("Name: {}".format(str(NewCredentials[i])))
        elif i == 1:
            print("Email: {}".format(str(NewCredentials[i])))
        elif i == 2:
            print("Password: {}".format(str(NewCredentials[i])))

    while UserChosen == False:
        areyousure = str(input("Are you sure? (Y/N): ")).lower()
        if areyousure == "y":
            print("Great! Your details have been uploaded to the cloud!")
            UserChosen = True

            # Open and edit data document

            Datafile = open("Credentials.txt", "a")

            for val in range(0, len(NewCredentials)):

                if val != len(NewCredentials):
                    Datafile.write(NewCredentials[val] + ", ")
                else:
                    Datafile.write(NewCredentials[val])

            Datafile.write("\n")

            Datafile.close()


        elif areyousure == "n":
            print("Ok! Sorry to hear that. Thanks for using our service today!")
            UserChosen = True
        else:
            print("That wasn't an option, sorry!")


    print("\n\n\n\n")
    Login()







def Login():
    time.sleep(1)

    ValidLogin = False

    DataFile = open("Credentials.txt", "r")

    print("Thanks for choosing to login! Please follow the following steps carefully!")

    while ValidLogin == False:
        Username = str(input("Please enter your username: "))
        Password = str(input("Please enter your password: "))

        for line in DataFile:
            line.strip("\n")
            values = line.split(", ")

            if values[0] == Username:
                if values[2] == Password:
                    print("Successfully Logged in!")
                    LoggedIn = True
                    GUsername = values[0]
                    GEmail = values[1]
                    ValidLogin = True



    DataFile.close()

    time.sleep(10)

# Main code -- where the user is asked whether they want to sign up or login

while LoggedIn == False and InMenu == True:
    print("Welcome, Please state whether you would like to sign in or sign up (L/S): ")
    answer = (str(input(""))).lower()
    if answer == "l":
        InMenu = False
        Login()
    elif answer == "s":
        InMenu = False
        SignUp()
    else:
        print("Invalid input detected. Please try again!\n")
        time.sleep(1)