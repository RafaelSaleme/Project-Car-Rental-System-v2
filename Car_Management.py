import os

Car_list = {}
user_input = ''

class Vehicles:
    def __init__(self, Brand, Model, Color, HorsePower, Price_day, Available, Maintenance_Service, Damage_Incident, Offer):
        self.Brand = Brand
        self.Model = Model
        self.Color = Color
        self.HorsePower = HorsePower
        self.Price_day = Price_day
        self.Available = Available
        self.Maintenance_Service = Maintenance_Service
        self.Damage_Incident = Damage_Incident
        self.Offer = Offer


while user_input.lower() != 'exit' :

    print("Car Management Menu\n\n")
    user_input = input("Add, See or exit\n")

    if user_input.lower() == 'add':
        
        Brand = input("Insert the car Brand\n")
        Model = input("Insert the car Model\n")
        Color = input("Insert the car Color\n")
        HorsePower = input("Insert the car HP(Horse Power)\n")
        Price_day = input("Insert the Rental Price\n")
        Available = input("Insert if the car is Available or not (Yes or No)\n")

        New_Car = Vehicles(Brand, Model, Color, HorsePower, Price_day, Available,"No Data", "No Data", "No")

        Car_list['aux'] = New_Car

        Car_ID = input("Set an ID for the car\n")
        Car_list[Car_ID] = Car_list['aux']
        del Car_list['aux']

        os.system('cls')
        print("The car was added to the car List\n")


    elif user_input.lower() == 'see':
        os.system('cls')
        print("Car list\n")
        print(Car_list)
        print("\n")

os.system('cls')
