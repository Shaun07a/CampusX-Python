# correct email - campusx@gmail.com
# password - 1234

email = input("Enter the email")
if '@' in email :
    password = input("Enter the password")

    if email == "campus@gmail.com" and password == "1234":
        print("Welcome")
    elif email == "campus@gmail.com" and password != "1234":
        print("Password Incorrect")
        password = input("Enter the password again")
        if password == "1234":
            print("Finally correct")
        else:
            print("Still Incorrect")
    else:
        print("Incorrect Credentials")
else:
    print("Invalid email format")