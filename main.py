from admin import admin
from user_fun import register_user, user_login, user_menu

while True:
    print('''Hey welcome to my food ordering app!
    Please select from the following options:
    Enter 1 for admin.
    Enter 2 for new user.
    Enter 3 for existing user.
    Enter 4 to exit.
    ''')
    user_option = input("Enter here: ")
    
    if user_option == "1":
        while True:
            admin_input = input("Login as admin y/n.\n")
            if admin_input.lower() == "y":    
                admin()
            elif admin_input.lower() == "n":
                print("Logged Out.\n")
                break
            else:
                print("Wrong option.\n")
    
    elif user_option == "2":
        result = register_user()
        if result == "sucess":
            print("You have been successfully registered.\n")
        if result == "already":
            print("Already a user.\n")
    
    elif user_option == "3":
        while True:
            user_input = input("Continue login y/n.\n")
            if user_input.lower() == "y":    
                res = user_login()
                if res[0] == "sucess":
                    user_menu(res[1])
                elif res[0] == "wrong_password":
                    print("Wrong password")
                elif res[0] == "not_found":
                    print("User not found")
                elif res[0] == "not_registered":
                    print("No user info available, first register to the app\n")
            elif user_input.lower() == "n":
                print("Logged Out.\n")
                break
            else:
                print("Wrong option\n")
            
    elif user_option == "4":
        print("Thank you for choosing us.\n")
        break
    
    else:
        print("Please enter the correct option.\n")
