import os
import Classes
import Car_Management

user_input = ''
Reg_Car = {}
Damage_Reports = {}
Incident_Reporting = {}

while user_input.lower() != '3' :

    print("Damage and Incident Reporting Menu\n\n")

    user_input = input("1. Add new Damage or Incident entry\n2. See Damage or Incident Reports\n3. Exit\n")

    if user_input.lower() == '1' :

        user_input = input("Insert wich entry you want to create:\n1. Damage\n2. Incident\n3. Return\n")

        if user_input.lower() == '1' :

            print("Add a new Damage entry\n\n")

            Car_ID = input("Insert the ID of the Car\n")
            Date = input("Insert the date when the car suffered the Damage\n")
            Details = input("Insert the Damage details\n")

            Reg_Car['Date'] = Date
            Reg_Car['Details'] = Details

            Car_Management.Car_list[Car_ID].Damage = Details
            Car_Management.Car_list[Car_ID].Damage_Date = Date

            Damage_Reports['aux'] = Reg_Car

            Damage_Reports[Car_ID] = Damage_Reports['aux']
            del Damage_Reports['aux']
            

            os.system("cls")
            print("New Damage entry added!\n")

        elif user_input.lower() == '2' :

            print("Add a new Incident entry\n\n")

            Car_ID = input("Insert the ID of the Car\n")
            Date = input("Insert the date of the Incident\n")
            Details = input("Insert the Incident details\n")

            Reg_Car['Date'] = Date
            Reg_Car['Details'] = Details

            Car_Management.Car_list[Car_ID].Incident = Details
            Car_Management.Car_list[Car_ID].Incident_Date = Date

            Incident_Reporting['aux'] = Reg_Car

            Incident_Reporting[Car_ID] = Incident_Reporting['aux']
            del Incident_Reporting['aux']

            os.system('cls')
            print("New Incident Entry added!\n")
    elif user_input.lower() == '2' :

        print("Damage and Incident Reports\n\n")

        user_input = input("1. See Damage Reports\n2. See Incident Reports\n")

        if user_input.lower() == '1' :

            os.system('cls')
            print(Damage_Reports)

        elif user_input.lower() == '2' :

            os.system('cls')
            print(Incident_Reporting)

os.system('cls')
