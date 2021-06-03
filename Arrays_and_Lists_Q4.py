# Arrays_and_Lists_Q4._Julie_O'Donnell_1236067_02/04/2021

# Write a program that enters a string containing a person's full name and then output their initials.

name = input("Please enter your full name: ")

full_name = name.split()
initials = ""

for j in range (len(full_name)):
    initials += full_name [j] [0]

print("Fullname: ", name)
print("Initials: ", initials)

