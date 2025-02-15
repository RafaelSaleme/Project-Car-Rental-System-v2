import os
import Classes

Car_list = {}
user_input = ''

os.system('cls')

while user_input.lower() != '3' :

    print("Car Management Menu\n\n")
    user_input = input("1. Add\n2. See\n3. Exit\n")

    if user_input.lower() == '1':
        
        Brand = input("Insert the car Brand\n")
        Model = input("Insert the car Model\n")
        Color = input("Insert the car Color\n")
        HorsePower = input("Insert the car HP(Horse Power)\n")
        Price_day = input("Insert the Rental Price\n")
        Available = input("Insert if the car is Available or not (Yes or No)\n")
        
        New_Car = Classes.Vehicle(Brand, Model, Color, HorsePower, Price_day, Available, "No Data", "",
                                   "No Data", "", "", "No Data", "", "No Data", "No Offers for this vehicle")

        Car_list['aux'] = New_Car

        Car_ID = input("Set an ID for the car\n")
        Car_list[Car_ID] = Car_list['aux']
        del Car_list['aux']

        os.system('cls')
        print("The car was added to the car List\n")


    elif user_input.lower() == '2':
        os.system('cls')
        print("Car list\n")
        [print(f"ID: {key}\n\n{value}\n\n") for key, value in Car_list.items()]
        print("\n")

os.system('cls')
