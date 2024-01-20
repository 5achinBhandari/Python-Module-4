
CorrectUsername = "python"
CorrectPassword = "rules"


attempts = 0

while attempts < 5:

    username = input("Enter username: ")
    password = input("Enter password: ")


    if username == CorrectUsername and password == CorrectPassword:
        print("Welcome!")
        break
    else:
        print("Access denied. Please try again.")
        attempts += 1


if attempts == 5:
    print("Access denied. You have exceeded the maximum number of login attempts.")
