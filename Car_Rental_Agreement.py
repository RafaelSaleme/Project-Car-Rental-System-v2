import os
import Car_Customer_List
import Car_Management

Agreements_list = {}
user_input = ''
user1 = ''
user2 = ''


while user_input.lower() != '4' :

    print("Rental Agreements Menu\n")

    user_input = input("1. Make a new agreement\n2. Cancel an agreement\n3. See Agreements\n4. Exit")


    if user_input.lower() == '1' :
        
        os.system('cls')
        print("New Agreement Menu\n\n")

        
        user1 = input("Insert your nickname\n")
        user2 = input("Insert the nickname of who you want to make an agreement\n")
        Car_ID = input("Insert the ID of the car you want to make an agreement\n")

        Agreements_list[Car_ID]['Buyer'] = user1
        Agreements_list[Car_ID]['Owner'] = user2

        os.system('cls')
        print("Agreement created!\n")
        

    elif user_input.lower() == '2' :

        os.system('cls')
        print("Cancel Agreement Menu")

        Car_ID = input("Insert the ID of the car you want to cancel the agreement\n")

        Agreements_list.pop(Car_ID)

        os.system("cls")
        print("Car Agreement Canceled!\n")
    
    elif user_input.lower() == '3' :
        
        os.system('cls')
        print("Agreements List\n")
        print(Agreements_list)






    