# Arrays_and_Lists_Q2._Julie_O'Donnell_1236067_01/04/2021

# Design a program which will ask the user to enter the date in the form dd/mm/yyyy. Example 23/08/2019.

# The date will be printed like below:

# Date: 23
# Month : 08
# Year: 2019

date = (input("Please enter a date in the form of dd/mm/yyyy: "))

date_split = date.split ("/")

print("Date: ", date_split[0])
print("Month: ", date_split[1])
print("Year: ", date_split[2])
