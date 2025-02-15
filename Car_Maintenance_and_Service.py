import os
import Classes
import Car_Management

user_input = ''
Reg_Car = {}
Maintenance_Record = {}
Service_Record = {}

while user_input.lower() != '3' :

    print("Maintenance and Services Menu\n\n")

    user_input = input("1. Add new maintenance or service entry\n2. See maintenance or service record\n3. Exit\n")

    if user_input.lower() == '1' :

        user_input = input("Insert wich entry you want to create:\n1. Maintenance\n2. Service\n3. Return\n")

        if user_input.lower() == '1' :

            print("Add a new Maintenance entry\n\n")

            Car_ID = input("Insert the ID of the Car\n")
            Date = input("Insert the date of the Maintenance\n")
            Details = input("Insert the details of the Maintenance\n")

            Reg_Car['Date'] = Date
            Reg_Car['Details'] = Details

            Car_Management.Car_list[Car_ID].Maintenance = Details
            Car_Management.Car_list[Car_ID].Maintenance_Date = Date

            Maintenance_Record['aux'] = Reg_Car

            Maintenance_Record[Car_ID] = Maintenance_Record['aux']
            del Maintenance_Record['aux']
            

            os.system("cls")
            print("New Maintenance entry added!\n")

        elif user_input.lower() == '2' :

            print("Add a new Service entry\n\n")

            Car_ID = input("Insert the ID of the Car\n")
            Date = input("Insert the date of the Service\n")
            Details = input("Insert the details of the Service\n")

            Reg_Car['Date'] = Date
            Reg_Car['Details'] = Details

            Car_Management.Car_list[Car_ID].Service = Details
            Car_Management.Car_list[Car_ID].Service_Date = Date

            Service_Record['aux'] = Reg_Car

            Service_Record[Car_ID] = Service_Record['aux']
            del Service_Record['aux']

            os.system('cls')
            print("New Service Entry added!\n")
    elif user_input.lower() == '2' :

        print("Maintenance and Service Records\n\n")

        user_input = input("1. See Maintenance Records\n2. See Services Records\n")

        if user_input.lower() == '1' :

            os.system('cls')
            print(Maintenance_Record)

        elif user_input.lower() == '2' :

            os.system('cls')
            print(Service_Record)

os.system('cls')
