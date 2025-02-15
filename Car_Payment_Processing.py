import os
from Classes import *
import Car_Management
import Car_Request
import Car_Customer_List

user_input = ''
Value_Deposit = ''
Bank = {}
Refund_requests = {}

while user_input.lower() != '4' :
    
    print("Payment Processing Menu\n\n")
          
    user_input = input("1. Payment\n2. Deposit\n3. Refund\n4. Exit\n")


    if user_input.lower() == '1' :

        os.system('cls')

        print("Payment Menu\n\n")

        Car_Payment_ID = input("Insert the ID of the car\n")

        User_Nickname= input("Insert the user Nickname\n")

        print(f"Total owed by {User_Nickname}: {Car_Management.Car_list[Car_Payment_ID].Price_day} \n")

        Value_Owned = Car_Management.Car_list[Car_Payment_ID].Price_day

        Car_Customer_List.Customers_List[User_Nickname].Debt += Value_Owned

        user_input = input('Procceed to payment page? (Yes or No)\n')
        if user_input.lower() == 'yes' : break

    elif user_input.lower() == '2' :
        
        os.system('cls')

        print("Deposit Menu\n\n")

        deposit_choice = input("1. Make a Deposit\n2. See Deposits\n")



        if deposit_choice == '1' :
        
            user_input = input("Insert the account Nickname you want to make a deposit\n")

            Value_Deposit = input("Insert the value you want to deposit\n")

            Car_Customer_List.Customers_List[user_input].Funds += Value_Deposit

            Bank[user_input] = Value_Deposit

            print(f"Deposited R$ {Value_Deposit} on {user_input} Account")

        elif deposit_choice == '2' :
            os.system('cls')
            print(Bank)

    elif user_input.lower() == '3' :

        os.system('cls')
        
        print("Refund Menu\n\n")

        user_input = input(f"Select the request you want to apply for a Refund\n {Car_Request.Requests}\n")

        Refund_requests[user_input] = input("Insert the reason you want to make a Refund.\n")

os.system('cls')










