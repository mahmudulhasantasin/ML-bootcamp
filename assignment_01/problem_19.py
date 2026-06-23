correct_username = "admin"
correct_password = "pass123"
username = input("Enter username: ")
password = input("Enter password: ")
if username == correct_username:
    if password == correct_password:
        print("Access Granted")
    else:
        print("Wrong Password")
else:
    print("User Not Found")
