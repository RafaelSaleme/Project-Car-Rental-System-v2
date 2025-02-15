import os
from Classes import *
import Car_Management
import Car_Customer_List


Requests = {}
Request = ''

while Request.lower() != '3' :

    print("Car Request Menu\n\n")

    Request = input("1. Make a new Request\n2. Cancel Request\n3. Exit\n")
    
    # New Request
    if Request.lower() == '1' : 
    
        os.system('cls')
        [print(f"ID: {key}\n\n{value}\n\n") for key, value in Car_Management.Car_list.items()]
    
        
        Car_Request_ID = input("Insert the ID of the car you want to request\n")
    

        if Car_Management.Car_list[Car_Request_ID].Available.lower() == 'yes' :

            os.system('cls')

            user_input = input("Insert your Nickname\n")

            Requests[Car_Request_ID] = user_input

            Car_Management.Car_list[Car_Request_ID].Available = 'No'
            Car_Customer_List.Customers_List[user_input].Last_Rent = Car_Request_ID
            os.system('cls')
            print("Car successfully requested!\n")
        
            

        elif Car_Management.Car_list[Car_Request_ID].Available.lower() == 'no' :
            os.system('cls')
            print("The car is already requested!\n")

    # Request Cancel
    elif Request.lower() == '2' :

        os.system('cls')
        [print(f"ID: {key}\n\n{value}\n\n") for key, value in Car_Management.Car_list.items()]
    

        Car_Request_ID = input("Insert the ID of the car you want to cancel the request\n")

        if Car_Management.Car_list[Car_Request_ID].Available.lower() == 'no' :
            os.system('cls')
            print("Car request successfully canceled!\n")
        
            Car_Management.Car_list[Car_Request_ID].Available = "Yes"

        elif Car_Management.Car_list[Car_Request_ID].Available.lower() == 'yes' :
            os.system('cls')
            print("There is no request for thi car!\n") 



os.system('cls')
