#Julie O'Donnell: 1236067 - Introduction to Selection Q5 - 18/03/2021


#ask user for their percentage grade

grade = int(input("What was your grade: "))

x = grade

#grade based upon a percentage grade

if x > 89 and x < 101:
    print("You will receive a 'High Distinction'")

if x > 79 and x < 90:
    print("You will receive a 'Distinction'")

if x > 69 and x < 80:
    print("You will receive a 'Credit'")

if x > 49 and x < 70:
    print("You will receive a 'Pass'")


