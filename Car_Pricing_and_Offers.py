import os
import Car_Management

user_input = ''
Cars_Discounts = {}
Cars_Special_Offers = {}
Modification_Discount = {}
Modification_SO = {}

while user_input.lower() != '4' :

    print("Pricing and Special Offers Menu\n\n")

    user_input = input("1. Manage Pricing and Special Offers\n2. See Pricing and Special Offers\n")
    os.system('cls')

    if user_input.lower() == '1':

        print("Pricing and Special Offers Menu\n\n")
        user_input = input("1. Manage Pricing\n2. Manage Discounts\n3. Manage Special Offers\n4. Exit\n")

        if user_input.lower() == '1':

            os.system('cls')
            print("Price Management Menu\n\n")
            
            user_input = input(f"Insert the ID of the car you want to change the price\n{Car_Management.Car_list}\n\n")
            New_Value = input("Insert the new price of the car\n")

            Car_Management.Car_list[user_input].Price_day = New_Value

            os.system('cls')
            print("Car price changed!\n")

        elif user_input.lower() == '2' :
            
            os.system('cls')
            print("Discounts Management Menu\n\n")

            Car_ID = input(f"Insert the ID of the car you want to add a Discount\n{Car_Management.Car_list}\n")
            New_Value = input("Insert the new price of the car with the Discount\n")
            Remaining_Duration = input("Insert the remaining duration of the Discount\n")

            Modification_Discount['Discounted Value'] = New_Value
            Modification_Discount['Remaining Duration'] = Remaining_Duration

            Car_Management.Car_list[Car_ID].Offer = f"This car has a discount, the current price is: {New_Value}"

            Cars_Discounts['aux'] = Modification_Discount
            Cars_Discounts[Car_ID] = Cars_Discounts['aux']
            del Cars_Discounts['aux']

            os.system('cls')
            print("Discount added to the list!\n")

        elif user_input.lower() == '3':

            os.system('cls')
            print("Special Offers Management Menu\n\n")

            Car_ID = input(f"Insert the ID of the car you want to add a Special Offer\n{Car_Management.Car_list}\n")
            New_Value = input("Insert the new price of the car\n")
            Remaining_Duration = input("Insert the remaining duration of the Special Offer\n")
            Special_Condition = input("Insert the Special Condition for the Special Offer\n")

            Modification_SO['Special Value'] = New_Value
            Modification_SO['Remaining Duration'] = Remaining_Duration

            Car_Management.Car_list[Car_ID].Offer = f"This car has a Special Offer:\nSpecial Price:{New_Value}\nCondition:{Special_Condition}"

            Cars_Special_Offers['aux'] = Modification_SO
            Cars_Special_Offers[Car_ID] = Cars_Special_Offers['aux']
            del Cars_Special_Offers['aux']

            os.system('cls')
            print("Special Offer added to the list!\n")
    
    elif user_input.lower() == '2':

        print("What would you like to see?\n\n")

        user_input = input("1. Discounts\n2. Special Offers\n")

        if user_input.lower() == '1' :

            os.system('cls')
            print(Cars_Discounts)

        elif user_input.lower() == '2':
            
            os.system('cls')
            print(Cars_Special_Offers)
os.system('cls')








    


