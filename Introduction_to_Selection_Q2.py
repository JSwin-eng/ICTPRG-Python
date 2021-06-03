#Julie O'Donnell: 1236067 - Introduction to Selection Q2 - 18/03/2021

#ask user for their year of birth

year_of_birth = int (input("What is your Year of birth: "))

legal_drinking_age = int (input("How old are you?: "))
print(legal_drinking_age)

x = (legal_drinking_age)

if x >= 18:
    print("Come in and have a drink")

if x < 18:
    print("Go away. Child.")

