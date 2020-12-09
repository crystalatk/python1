count = 0
user_input = input("How high would you like to count? ")

try:
    MAX = int(user_input)
    while count <= MAX:
        print(count)
        count += 1
except ValueError:
    print("Please run the program again, this time with a number!")
