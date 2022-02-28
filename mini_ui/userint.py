# USER INTERFACE PROGRAM

print("Welcome to this program!")
print("This program is a simulation of a user interface on a website!")
print("It will start with a default username and password, and you will have the opportunity to make your own!")
print("--------------------------------------------------------------------------------------------------------")

username = "coolusername_123"
password = "epic_code123"

print("The orginial username is: ", username)
print("The original password is: ", password)

enterusername = input("Enter the OG username")
enterpassword = input("Enter the OG password")

if enterusername == username and enterpassword == password:
    print("You are succesfully logged in.")
    newaccountyorn = input("Would you like to make a new account now?")
    if newaccountyorn == "Yes" or "yes":
        global newuser
        global newpass
        print("Alright! Lets do this.")
        newuser = input("What would you like your new username to be?")
        newpass = input("What would you like your new password to be?")
        ogusername = newuser
        ogpass = newpass
        print("Alright! You new username is:", ogusername, "and your new password is:", ogpass)
        print("NOTE: The OG Password has been overridded, so it will not work anymore. You can now only log in with this username and password.")
else:
    print("Incorrect Password. Access Denied.")
    print('---------------------------------')