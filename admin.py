import json
from datetime import datetime as dt
from json import JSONDecodeError

class Admin:

    def add_item(self):
        name = input("Enter the name of the food item\n")
        quantity = input("Enter the quantity of the food item\n")
        price = int(input("Enter the price of the food item\n"))
        discount = input("Enter the discount on the food item\n")
        try:
            file1 = open("food_items.json","r+")
            content = json.load(file1) 
        except FileNotFoundError:
            file1 = open("food_items.json","w+")
            content = {1:{"Name":"Tandoori Chicken","Quantity":"(4 piece)","Price":240,"Discount":"10%"},
            2:{"Name":"Vegan Burger", "Quantity":"(1 Piece)", "Price":320,"Discount":"8%"},
            3:{"Name":"Tuffle Cake", "Quantity":"(500 gm)", "Price":900,"Discount":"16%"}}
            json.dump(content,file1,indent=4)
        except JSONDecodeError:
            content = {1:{"Name":"Tandoori Chicken","Quantity":"(4 piece)","Price":240,"Discount":"10%"},
            2:{"Name":"Vegan Burger", "Quantity":"(1 Piece)", "Price":320,"Discount":"8%"},
            3:{"Name":"Tuffle Cake", "Quantity":"(500 gm)", "Price":900,"Discount":"16%"}}
            json.dump(content,file1,indent=4)  
        
        content[len(content)+1] = {"Name":name,"Quantity":quantity,"Price":price,"Discount":discount}
        file1.seek(0)
        file1.truncate()
        json.dump(content,file1,indent=4)
        file1.close()
        return "sucess"

    def edit_food_items(self, id):
        try:
            file1 = open("food_items.json","r+")
            food_items = json.load(file1) 
        except FileNotFoundError:
            file1 = open("food_items.json","w+")
            food_items = {1:{"Name":"Tandoori Chicken","Quantity":"(4 piece)","Price":240,"Discount":"10%"},
            2:{"Name":"Vegan Burger", "Quantity":"(1 Piece)", "Price":320,"Discount":"8%"},
            3:{"Name":"Tuffle Cake", "Quantity":"(500 gm)", "Price":900,"Discount":"16%"}}
            json.dump(food_items,file1,indent=4)
        except JSONDecodeError:
            food_items = {1:{"Name":"Tandoori Chicken","Quantity":"(4 piece)","Price":240,"Discount":"10%"},
            2:{"Name":"Vegan Burger", "Quantity":"(1 Piece)", "Price":320,"Discount":"8%"},
            3:{"Name":"Tuffle Cake", "Quantity":"(500 gm)", "Price":900,"Discount":"16%"}}
            json.dump(food_items,file1,indent=4)  
        para = input("What do you want to edit? (Name, Quantity, Price, Discount)\n")
        if para.lower() == "name":
            new = input("Enter the new name\n")
            if new == food_items[id]["Name"]:
                print("You have entered the same name\n")
            else:
                food_items[id]["Name"] = new

        elif para.lower() == "quantity":
            new = input("Enter the new quantity\n")
            if new == food_items[id]["Quantity"]:
                print("You have entered the same quantity\n")
            else:
                food_items[id]["Quantity"] = new

        elif para.lower() == "price":
            new = int(input("Enter the new price\n"))
            if new == food_items[id]["Price"]:
                print("You have entered the same price\n")
            else:
                food_items[id]["Price"] = new

        elif para.lower() == "discount":
            new = int(input("Enter the new discount.\n"))
            if new == food_items[id]["Discount"]:
                print("You have entered the same discount.\n")
            else:
                food_items[id]["Discount"] = new

        else:
            print("You have entered wrong detail\n")

        file1.seek(0)
        file1.truncate()
        json.dump(food_items,file1,indent=4)
        file1.close()
        return "sucess"

    def list_of_items(self):
        try:
            file1 = open("food_items.json","r+")
            food_items = json.load(file1) 
        except FileNotFoundError:
            file1 = open("food_items.json","w+")
            food_items = {1:{"Name":"Tandoori Chicken","Quantity":"(4 piece)","Price":240,"Discount":"10%"},
            2:{"Name":"Vegan Burger", "Quantity":"(1 Piece)", "Price":320,"Discount":"8%"},
            3:{"Name":"Tuffle Cake", "Quantity":"(500 gm)", "Price":900,"Discount":"16%"}}
            json.dump(food_items,file1,indent=4)
            
        except JSONDecodeError:
            file1 = open("food_items.json","w+")
            food_items = {1:{"Name":"Tandoori Chicken","Quantity":"(4 piece)","Price":240,"Discount":"10%"},
            2:{"Name":"Vegan Burger", "Quantity":"(1 Piece)", "Price":320,"Discount":"8%"},
            3:{"Name":"Tuffle Cake", "Quantity":"(500 gm)", "Price":900,"Discount":"16%"}}
            json.dump(food_items,file1,indent=4)
            file1.close()
        
        for key,value in food_items.items():
            print(f"\nFoodID: {key}")
            for j,k in value.items():
                if j.lower()=="price":
                    print(f"{j}:- INR {k}")   
                else:
                    print(f"{j}:- {k}") 

    def remove_items(self, id):
        file1 = open("food_items.json","r+")
        food_items = json.load(file1) 
        if id in food_items:
            food_items.pop(id)
            file1.seek(0)
            file1.truncate()
            json.dump(food_items,file1,indent=4)
            print("Food item has been removed")
        else:
            print("Food ID not found.")
        file1.close()

    def stock(self):
        print("Stock Left:\nTandoori chicken : 10kg\nVegan Burger : 50 pieces\nTuffle Cake : 50 pieces\n")

def admin():
    b2 = Admin()
    admin_name = "Pravin"
    admin_password = "1234"
    input_name = input("Enter admin name:(Pravin)\n")
    input_password = input("Enter admin password:(1234)\n")
    if input_name == admin_name and input_password == admin_password:
        print("\nHey you have been logged in  as admin!")
        while True:
            option = input('''Select from the following options:
Enter 1 to add food item.
Enter 2 to check stock left.
Enter 3 to see the list of food items.
Enter 4 to edit food item using food ID.
Enter 5 to remove food item using food ID.
Enter 6 to exit
''')
            if option == "1":
                response1 = b2.add_item()
                if response1 == "success":
                    print("Food item added successfully\n")
                else:
                    print("Food item added successfully\n")
        
            elif option == "2":
                b2.stock()

            elif option == "3":
                b2.list_of_items()
        
            elif option == "4":
                id1 = input("Enter the food ID of the food item which you want to edit:\n")
                response2 = b2.edit_food_items(id1)
                if response2 == "success":
                    print("Food item edited successfully.\n")
                else:
                    print("Food item edited successfully.\n")

            elif option == "5":
                id = input("Enter the food ID of the food item you want to remove\n")
                b2.remove_items(id)
            
            elif option == "6":
                break
            else:
                print("Wrong option.\n")
    else:
        print("Wrong admin details.")
        return None
