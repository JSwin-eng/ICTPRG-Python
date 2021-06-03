#Julie O'Donnell: 1236067 - Introduction to Selection Q4 - 18/03/2021

# accepted username and password combinations

username_password1 = "bob password1234"
username_password2 = "fred happyPass122"
username_password3 = "lock passwithlock44"

#ask user for their username and password

username_password = str (input("What is your username and password: "))

#ensure password only works with corresponding username and password combinations

if username_password == username_password1:
    print("Access Granted!")


elif username_password == username_password2:
    print("Access Granted!")


elif username_password == username_password3:
    print("Access Granted!")

else:
    print("Access Denied!")








