
import admin as aa
from user import User

uhh = User(str, str, str, str, str)

inp = int(input("Where You want to Register or login select 1.Admin and 2.Register and 3.Exit"))
#String--Admin and User
#int-1 for admin and 2 for user and 3 for exit
if inp == 1:
    Username = input("Enter the username of admin: ")
    Password = input("Enter the password of admin: ")
    if aa.admin_keys[Username] == Password:
        print("*****You're successfully logged inn*****")
        admin_crawler = True
        while admin_crawler:
            adm_choice = int(input("Choose the options of admin panel 1.ADD NEW ITEM 2.EDIT ITEM 3.VIEW INVENTORY 4.REMOVE ITEM 5.EXIT"))
            if adm_choice == 1:
                aa.add_new_item()
            elif adm_choice == 2:
                aa.edit_from_item()
            elif adm_choice == 3:
                aa.show_inven()
            elif adm_choice == 4:
                aa.remove_item()
            elif adm_choice == 5:
                print(f"You're Exit to the admin panel{Username}")
                admin_crawler = False
            else:
                print("This is the wrong selection please select valid option")
    else:
        print("These are the wrong credentials! SORRY!!!")
elif inp == 2:
    print("Welcome to the user panel")
    username = input("Enter the username here: ")
    password = input("Enter the password here: ")
    phoneno = input("Enter the phone number here: ")
    email = input("Enter the email here: ")
    address = input("Enter the address here: ")
    if User.register(username,phoneno,email,address,password):
        print(f"You are rohlogged in successfully {username}")
        user_crawler = True
        while user_crawler:
            usr_choice = int(input(f"{username}, Enter the option 1.Place new order 2.Order history 3.Exit"))
            if usr_choice == 1:
                uhh.place_order()
            elif usr_choice == 2:
                print(f"Here is your order history, {username}")
                print(uhh.order_history)
            elif usr_choice == 3:
                user_crawler = False
                print("You're Successfully looged out")
            else:
                print("You choose the invalid option")
    else:
        print("These are the wrong credentials! SORRY!!!")
if inp==3:
    exit()

else:
    username = input('Enter username')
    password = input('Enter password')
    if username in aa.admin_keys:
        print('User is already registered , please login')
    else:
        aa.admin_keys[username] = password
    print('User Registered successfully')





