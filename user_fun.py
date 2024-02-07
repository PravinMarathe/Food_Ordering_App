import json
import re
from datetime import datetime as dt
from json import JSONDecodeError

class User:
    regex_name = "^[A-Za-z]+\s?[a-z]*"
    regex_phn = "^[0-9]{10}$"
    regex_email = "^[a-z0-9]+[\.\-_]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    regex_password = "^(?=.*?[A-Z])(?=(.*[a-z]){1,})(?=(.*[\d]){1,})(?=(.*[\W]){1,})(?!.*\s).{8,}$"
    regex_address = "[\w',-\\/.\s]"

    def __init__(self):    
        self.name = "XYZ"
        self.phn = "1234567890"
        self.email = "xyz@mail.com"
        self.address = "house no.,area,city,state"
        self.password = "$ampLePassword123"
        self.orders = []

    def add_name(self):
        while True:
            name = input("Enter your full name.\n")    
            if bool(re.search(User.regex_name,name)):
                self.name =name
                break
            else:
                print("Enter valid name.\n")

    def add_phn(self):
        while True:
            phn = input("Enter you phone number.\n")
            if bool(re.search(User.regex_phn,phn)):
                self.phn = phn
                break
            else:
                print("Enter correct phone number.\n")

    def add_email(self):
        while True:
            email = input("Enter your Email.\n")
            if bool(re.search(User.regex_email,email)):
                self.email = email
                break
            else:
                print("Enter valid email address.\n")

    def add_address(self):
        while True:
            address = input("Enter your full address.\n")
            if bool(re.search(User.regex_address,address)):
                self.address = address
                break
            else:
                print("Enter valid address.\n")

    def set_password(self):
        while True:
            password = input("Enter your password.\n")
            if bool(re.search(User.regex_password,password)):
                self.password = password
                break
            else:
                print('''Enter a valid password.
(Should contain one capital and small letter, one special character, one number and should be of minimum length 8.''')    



    def list_of_food(self):
        try:
            file1 = open("food_items.json","r+")
            food_items = json.load(file1) 
        except FileNotFoundError:
            file1 = open("food_items.json","w+")
            food_items = {1:{"Name":"Tandoori Chicken","Quantity":"(4 piece)","Price":240,"Discount":"10%"},
            2:{"Name":"Vegan Burger", "Quantity":"(1 Piece)", "Price":320,"Discount":"8%"},
            3:{"Name":"Tuffle Cake", "Quantity":"(500 gm)", "Price":900,"Discount":"16%"}}
            
        except JSONDecodeError:
            food_items = {1:{"Name":"Tandoori Chicken","Quantity":"(4 piece)","Price":240,"Discount":"10%"},
            2:{"Name":"Vegan Burger", "Quantity":"(1 Piece)", "Price":320,"Discount":"8%"},
            3:{"Name":"Tuffle Cake", "Quantity":"(500 gm)", "Price":900,"Discount":"16%"}}
            
            
        for key,value in food_items.items():
            print(f"\nFoodID: {key}")
            for j,k in value.items():
                if j.lower()=="price":
                    print(f"{j}:- INR {k}") 
                
                elif j.lower()=="discount":
                    continue                  
                else:
                    print(f"{j}:- {k}")    
        json.dump(food_items,file1,indent=4)
        file1.close()

    def place_order(self, food_id, user_mail):
        try:
            file = open("user_info.json","r+")
            content5 = json.load(file) 
        except JSONDecodeError:
            content5 = {}
    
        list_of_order = content5[user_mail]["orders"]
        now = dt.now()
        date_tm = now.strftime("%m/%d/%Y, %H:%M:%S")
        dictt = {date_tm:food_id}
        list_of_order.append(dictt) 
        content5[user_mail]["orders"] = list_of_order
        file.seek(0)
        file.truncate()
        json.dump(content5,file,indent=4)
        file.close()
        return "sucess"

def update_profile(user_mail):
    file8 = open("user_info.json","r+")
    content8 = json.load(file8)
    user_in = input("What do you want to update.(Name, Phone, Address, Password)\n")
    if user_in.lower() == "name":
        new = input("Enter the new name\n")
        if new == content8[user_mail]["name"]:
            print("You have entered the same name\n")
        else:
            content8[user_mail]["name"] = new
    
    elif user_in.lower() == "phone":
        new = input("Enter the new phone number.\n")
        if new == content8[user_mail]["phn"]:
            print("You have entered the same phone number.\n")
        else:
            content8[user_mail]["phn"] = new

    elif user_in.lower() == "address":
        new = input("Enter the new address\n")
        if new == content8[user_mail]["address"]:
            print("You have entered the same address\n")
        else:
            content8[user_mail]["address"] = new    

    elif user_in.lower() == "password":
        new = input("Enter the new password\n")
        if new == content8[user_mail]["password"]:
            print("You have entered the same password\n")
        else:
            content8[user_mail]["password"] = new
    
    else:
        print("Invalid option.\n")

    file8.seek(0)
    file8.truncate()
    json.dump(content8,file8,indent=4)
    file8.close()
    return "sucess"

def register_user():
    b1 = User()
    try:
        file = open("user_info.json","r+")
        content = json.load(file) 
    except FileNotFoundError:
        file = open("user_info.json","w+")
        content = {}
    except JSONDecodeError:
        content = {}  
    b1.add_name()
    b1.add_phn()
    b1.add_email()
    b1.add_address()
    b1.set_password()
    try:
        if b1.__dict__["email"] not in content.keys():
            content[b1.__dict__["email"]] = b1.__dict__
            file.seek(0)
            file.truncate()
            json.dump(content,file,indent=4)
            file.close()
            return "sucess"

        elif b1.__dict__["email"] in content.keys():
            file.close()
            return "already"
    except KeyError:    
        content["email"] = b1.__dict__
        file.seek(0)
        file.truncate()
        json.dump(content,file,indent=4)
        file.close()    
        return "sucess"

def user_login():
    try:
        file = open("user_info.json","r+")
        content4 = json.load(file) 
    except FileNotFoundError:
        file = open("user_info.json","w+")
        file.close()
        return ["not_registered"]
    except JSONDecodeError:
        file.close()
        return ["not_registered"]
    login_email = input("Enter your email.\n")
    login_password = input("Enter password.\n")

    if login_email in content4:
        if login_password == content4[login_email]["password"]:
            print(f"\nHey {content4[login_email]['name']}!")
            file.close()
            return ["sucess",login_email]
        else:
            file.close()
            return ["wrong_password"]
    else:
        file.close()
        return ["not_found"]

def user_menu(user_mail):
    b1 = User()
    while True: 
        print('''What do you wanna do?
Enter 1 to place new order.
Enter 2 to see order history.
Enter 3 to update profile
Enter 4 to exit   
    ''')
        option_user = input("Enter here: ")
        if option_user == "1":
            file1 = open("food_items.json","r+")
            content5 = json.load(file1)
            for i in content5:
                print(f"{i}. {content5[i]['Name']} ({content5[i]['Quantity']}) [INR {content5[i]['Price']}]")
                file1.close()
            user_optn = input("Enter your order (give fooID seperated by commas)\n").split(",")
            response7 = b1.place_order(user_optn, user_mail)
            if response7 == "sucess":
                print("Your order is sucessfully palced!\n")
            else:
                print("Unable to place order currently\n")

        elif option_user == "2":
            file9 = open("user_info.json")
            content9 = json.load(file9)
            print("Here's your order history:")
            for i in content9[user_mail]["orders"]:
                for key,value in i.items():
                    print(f"{key} : {value}")
            file9.close()
        
        elif option_user == "3":
            response8 = update_profile(user_mail)
            if response8 == "sucess":
                print("Your profile has been sucessfully updated\n")
            else:
                print("Unable to update profile\n")

        elif option_user == "4":
            break
        
        else:
            print("Wrong option!\n")
