from random import randint 
from colorama import Fore
import json 

list_id_cards = {}

with open("data.json") as F:
    Dict = json.load(F)

for key, value in Dict.items():
    
    list_id_cards.setdefault(value["card_num"], key)

###################################################

def read_or_write_data_as_dict(new_dict: dict={}, mode="r"):
        
    if mode == "r":
        with open("data.json") as F:
            Dict = json.load(F)
    
        return Dict 
    
    elif mode == "w":
        with open("data.json", "w") as F:
            json.dump(new_dict, F)
    
###################################################

def Print(string, color="r"):
    
    if color == "r":
        print(Fore.RED + string + Fore.RESET) 
    
    elif color == "g":
        print(Fore.GREEN + string + Fore.RESET)  
    
    elif color == "b":
        print(Fore.BLUE + string + Fore.RESET) 

###################################################

def read_admin_password():
    with open("admin.json") as F:
        Dict = json.load(F)
    
    return Dict["password"]

###################################################

static_card = "60379917"

###################################################

def password_generator():
    return randint(1000, 9999) 

###################################################

def id_card_generator():
    num = randint(10000000, 99999999)
    new_num = str(static_card) + str(num)
    return int(new_num)

###################################################

def m_accept_or_reject_loan():
    pass 

###################################################

def m_release_user():
    
    input_id = input("Enter the id number that you want to ban: ")
        
    Dict = read_or_write_data_as_dict()
    
    Dict[input_id]["status"] = True 
    
    read_or_write_data_as_dict(Dict, "w")

###################################################

def m_ban_user():
    
    input_id = input("Enter the id number that you want to ban: ")
        
    Dict = read_or_write_data_as_dict()
    
    Dict[input_id]["status"] = False
    
    read_or_write_data_as_dict(Dict, "w")

###################################################

def m_change_password():
    
    input_id = input("Enter the id number that you want to change password: ")
    
    new_pass = int(input(f"Enter the new password for '{input_id}': "))
    
    Dict = read_or_write_data_as_dict()
    
    Dict[input_id]["password"] = new_pass
    
    read_or_write_data_as_dict(Dict, "w")

###################################################

def remove_account():
    
    input_id = input("Enter the id number that you want to remove: ")
    
    Dict = read_or_write_data_as_dict()
    
    list_id_cards.pop(Dict[input_id]["card_num"])
    Dict.pop(input_id)
    
    read_or_write_data_as_dict(Dict, "w")

###################################################

def unlimited_transfer(mode="admin", source_id_card=0):
    
    x = read_or_write_data_as_dict()
    
    if mode == "admin":
        source_id_card = int(input("Enter the source id card: "))
    
    destination_id_card = int(input("Enter the destination id card: "))
        
    if source_id_card in list_id_cards:
        
        if destination_id_card in list_id_cards:
            
            amount = int(input("how much money do you want to transfer: "))
            
            if mode == "admin":
                
                if amount <= x[list_id_cards[source_id_card]]["balance"]:
                    
                    x[list_id_cards[source_id_card]]["balance"] -= amount
                    
                    x[list_id_cards[destination_id_card]]["balance"] += amount
                    
                else:
                    Print("\nout of balance\n")
            
            else:
                
                if amount <= x[list_id_cards[source_id_card]]["balance"]:
                    
                    if amount <= 10000:
                        # Print("\n\nhey hey i am here\n\n", "b")
                        # print(Dict[list_id_cards[source_id_card]]["balance"])
                        x[list_id_cards[source_id_card]]["balance"] -= amount
                        # print(Dict[list_id_cards[source_id_card]]["balance"])
                        x[list_id_cards[destination_id_card]]["balance"] += amount
                        # print(Dict)
                        read_or_write_data_as_dict(x, "w")
                    else:
                        Print("\nout of range\n")
                    
                else:
                    Print("\nout of balance\n")
            
        else:
            Print("\ninvalid destination !\n")
    
    else:
        Print("\nwe dont have this source id card in our database !\n")
    
    
    
###################################################

def manage_account():
    
    while True:
        
        print("\n1- change password")
        print("2- ban user")
        print("3- release user")
        print("4- remove account")
        print("5- accept/reject loan")
        print("6- exit")

        option = input("Enter your option: ")
        
        if option == "1":
            m_change_password()
            
        elif option == "2":
            m_ban_user()
        
        elif option == "3":
            m_release_user() 
        
        elif option == "4":
            remove_account()
        
        elif option == "5":
            m_accept_or_reject_loan()
        
        elif option == "6":
            Print("\nreturn to admin panel\n", "g")
            break 
            
        else:
            Print("\ninvalid input ! try again !\n")

###################################################

def create_account():
    
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    
    while True:
        test_ID = int(input("Enter your id number: "))
        if test_ID not in read_or_write_data_as_dict():
            ID = test_ID
            break 
        else:
            Print("\nalready exist ! we had this id in our database !\n")
    
    balance = int(input("Enter your current balance: "))
    
    while True:
        test_id_card = id_card_generator()
        if test_id_card not in list_id_cards:
            id_card = test_id_card
            break 
    
    list_id_cards.setdefault(id_card, ID)
    
    four_digit_password = password_generator()
    
    Dict = read_or_write_data_as_dict()
    
    Dict[ID] = {"fname":fname,
                "lname":lname,
                "ID":ID,
                "balance":balance,
                "card_num":id_card,
                "password":four_digit_password,
                "status":True}
    
    read_or_write_data_as_dict(Dict, "w")

###################################################

def admin_panel():
    
    
    while True:
        
        print("\n1- create account")
        print("2- manage account")
        print("3- unlimited transfer")
        print("4- remove account")
        print("5- exit")
        
        option = input("Enter your option: ")
        
        if option == "1":
            create_account()
            
        elif option == "2":
            manage_account()
        
        elif option == "3":
            unlimited_transfer()
        
        elif option == "4":
            remove_account()
        
        elif option == "5":
            Print("\nend of program\n", "g"); break
        
        else:
            Print("\ninvalid input ! try again !\n") 

###################################################

def user_panel(ID):
    
    Dict = read_or_write_data_as_dict()
    
    while True:
        
        print("\n1- limited transfer")
        print("2- draw money")
        print("3- change password")
        print("4- request for loan")
        print("5- exit")
        
        option = input("Enter your option: ")
        
        if option == "1":
            unlimited_transfer("user", Dict[ID]["card_num"])
            
        elif option == "2":
            manage_account()
        
        elif option == "3":
            m_change_password()
        
        elif option == "4":
            pass
        
        elif option == "5":
            Print("\nend of program\n", "g"); break
        
        else:
            Print("\ninvalid input ! try again !\n") 
    
    read_or_write_data_as_dict(Dict, "w")

###################################################

while True: 
    
    print("\n1- admin panel")
    print("2- user panel")
    print("3- exit")
    
    Dict = read_or_write_data_as_dict()
    
    option = input("Enter your option: ")
    
    if option in ["admin", "1"]:
        password = input("Enter admin password: ")
        if password == read_admin_password():
            Print("\nwelcome to admin panel\n", "g")
            admin_panel()
            
        else:
            Print("\nincorrect password ! good bye !\n")
        
    elif option in ["user", "2"]:
        
        input_id = input("Enter your id: ")
        
        if input_id in Dict:
            
            if Dict[input_id]["status"]:
            
                counter = 3
                
                while counter >= 0:
                    
                    if counter == 0:
                        Print("\nyour account got banned !\n") 
                        Dict[input_id]["status"] = False 
                        break 
                        
                    password = int(input("Enter your password: "))
                    
                    if password == Dict[input_id]["password"]:
                        Print("\nwelcome to user panel\n", "g")
                        read_or_write_data_as_dict(Dict, "w")
                        user_panel(input_id)
                        break 
                    
                    elif counter != 0:
                        Print("\nincorrect password ! try again\n")
                        counter -= 1
                
            else:
                Print("\nyour account is banned !\n")

        
        else:
            Print("\nwe dont have this id in our database\n") 
        
    
    elif option in ["exit", "3"]:
        Print("\nend of program\n", "g"); break 
    
    else:
        Print("\ninvalid input ! try again !\n")
    
    

