import os
from Classes import *
import Car_Customer_List

user_input = ''
User_Feedbacks = []
New_Feedback = {}

while user_input != '3' :
    
    print("User Feedback and Review Menu\n\n")

    user_input = input("1. Submit Feedback and Review\n2. See Feebacks and Reviews\n3. Exit\n")

    if user_input.lower() == '1':
        
        print("Feedback and Review Submit Menu\n\n")

        New_Feedback['Nickname'] = input("Insert your nickname\n")
        New_Feedback['Date'] = input("Insert the date you are writing this feedback\n")
        New_Feedback['Car ID'] = input("Insert the Car ID form the car you rented\n")
        New_Feedback['Feedback'] = input("Insert your Feedback\n")

        Car_Customer_List.Customers_List[New_Feedback['Nickname']].Reviews = f"{New_Feedback['Date']}: Rented {New_Feedback['Car ID']}\nFeedback: {New_Feedback['Feedback']}"

        User_Feedbacks.append(New_Feedback)
        os.system('cls')
        print("Feedback and Review Submitted!")


    elif user_input.lower() == '2':
        os.system('cls')
        print(User_Feedbacks)

os.system('cls')

