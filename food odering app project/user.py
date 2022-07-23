
import numbers
import admin as ad

#a=User(,,,,)#
#b=User(,,,)
#after a -login_info={"a":'a'}
#after b -login_info={"a":'a','b':'b'}
login_info = {}
class User:
    

    def __init__(self, name, phoneno, email, address, password):
        self.name = name
        self.number = phoneno
        self.email = email
        self.address = address
        self.password = password
        self.profile={"Name":name}
        self.order_history = {}
    
    def register(name,phoneno,email,address,password):
        login_info[name] = name
        login_info[phoneno] = phoneno
        login_info[email] = email
        login_info[address] = address
        login_info[password] = password
        inp = int(input('User successfully registered , to login press 1 '))
        if inp==1:
            username = input('Enter Username')
            paword =input('Enter password')
            if name==username and password==paword:
                print("You're are successfully logged in.....")
                return True
            else:
                print("SORRY! These are the Wrong Credentials")
                return False
            

    

    def place_order(self):
        print("What you want to order here in the Inventory")
        print(ad.show_inven())
        user_choice = int(input("If you want to order then select 1.YES 2.NO"))
        if user_choice == 1:
            n=int(input("Enter how many items do you want to Order"))
            x=0
            for i in range(n):
             
             itemid = int(input("Enter the Item id here: "))
             quan = int(input("Enter the quantity of the item: "))
             x += ad.inven[itemid]["Price"] * quan
             self.order_history[itemid] = {
                    "Item Name": ad.inven[itemid]["ItemName"],
                    "Price": ad.inven[itemid]["Price"],
                    "Quantity": quan
                } 
            again_ask = input("Are you still want to order this Enter YES or NO")
            if again_ask == "YES":
             
                print(f"It costs you {x}INR in total")
                print("You're all set for this order")


                print("You're order is successfully placed")

            elif again_ask == "NO":
                print("This Order is cancelled!! You can look once more")
            else:
                print("Invalid choice")
        elif user_choice == 2:
            print("You select 2 option so we cancelled this")
        else:
            print("Enter the invalid choice")

#def cnu()
    def order_history_see(self):
        print(self.order_history)


    def update_profile(self):
        print("Update Profile Here <-------")
        email=input("Enter Your Mail-id ")
        if email in User.login_info.keys():
            print("Email Matched !!!!1")
            del User.login_info[email]


            new_email=input("Enter new Email")
            new_name = input("Enter new  Name ")
            new_phone_no = int(input("Enter new  Phone No "))
            new_Address = input("Enter new  Address ")
            new_password = input("Enter new  Password ")

            User.login_info[new_email] = {'Email': new_email,
                                                    'Full_Name': new_name,
                                                    'Phone_no': new_phone_no,
                                                    'Address': new_Address,
                                                    'Password': new_password,
                                                    }
            print("Profile Updated Successfully --------")

        else :
            print("Email not Registered <--- Please Try Again  ")

