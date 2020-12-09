# print("****2*****")

# name = input("What is your name? ")
# print("HELLO, %s!" % name.upper())
# length_of_name = len(name)
# print(f"YOUR NAME HAS {length_of_name} LETTERS IN IT! AWESOME!")

# print("****3****")

# print("Please fill in the blanks below:\n__(name)__'s favorite subject in school is __(school)__.")
# name = input("What is the name you would like to use? ")
# subject = input("What subject is the favorite? ")
# print(f"{name}'s favorite subject in school is {subject}.")

# print("****4****")
# day = 7
# while day < 0 or day > 6:
#     try:
#         day = int(input("Day (0-6)? "))
#         if day == 0:
#             print("Sunday")
#         elif day == 1:
#             print("Monday")
#         elif day == 2:
#             print("Tuesday")
#         elif day == 3:
#             print("Wednesday")
#         elif day == 4:
#             print("Thursday")
#         elif day == 5:
#             print("Friday")
#         elif day == 6:
#             print("Saturday")
#         else:
#             print("\nNo!\nPlease pick a number between 0 and 6\n")
#     except ValueError:
#         print("\nDon't be a dummy! You must choose a number.\nPlease try again.\n")
#         day = 8


print("*****5*****")

day = 7
while day < 0 or day > 6:
    try:
        day = int(input("Day (0-6)? "))
        if day == 0 or day == 6:
            print("Sleep in!")
        elif day >= 7 or day < 0:
            print("\nNo!\nPlease pick a number between 0 and 6\n")
        else:
            print("Go to Work!")
    except ValueError:
        print("\nDon't be a dummy! You must choose a number.\nPlease try again.\n")
        day = 8


print("****6****")
