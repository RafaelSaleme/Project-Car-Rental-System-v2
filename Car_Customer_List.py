import os
import Classes

Customers_List = {}

userInput = ''

while userInput.lower() != '3':
    
    
    print('Profile Menu\n\n')
    userInput = input('1. Add\n2. See\n3. Exit\n')
    
    if userInput.lower() == '1':
       
        os.system('cls')
        
        Name = input("Insert a name\n")
        ID = input("Insert a ID\n")
        Nickname = input("Insert a nickname\n")

        Customer = Classes.Customer(ID, Name, Nickname, "0", "0", "No Data", "No Data")

        Customers_List[Nickname] = Customer

        os.system('cls')

        print("Profile Created!\n")
    
    elif userInput.lower() == '2':
        os.system('cls')
        print("Customer List\n")
        [print(f"{value}\n\n") for key, value in Customers_List.items()]
        

os.system('cls')