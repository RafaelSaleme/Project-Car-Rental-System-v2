class Maintenance:
    def __init__(self, Maintenance_Date, Maintenance_Details):
        self.Maintenance_Date = Maintenance_Date
        self.Maintenance_Details = Maintenance_Details

    def __str__(self):
        return f"{self.Maintenance_Date}: {self.Maintenance_Details}\n"
    
class Service:
    def __init__(self, Service_Date, Service_Details):
        self.Service_Date = Service_Date
        self.Service_Details = Service_Details

    def __str__(self):
        return f"{self.Service_Date}: {self.Service_Details}"

class Damage_and_Incident:
    def __init__(self, Damage_Date, Damage_Details, Incident_Date, Incident_Details):
        self.Damage_Date = Damage_Date
        self.Damage_Details = Damage_Details
        self.Incident_Date = Incident_Date
        self.Incident_Details = Incident_Details

class Customer:
    def __init__(self, ID, Name, Nickname, Debt, Funds, Reviews, Last_Rent):
        self.ID = ID
        self.Name = Name
        self.Nickname = Nickname
        self.Debt = Debt
        self.Funds = Funds
        self.Reviews = Reviews
        self.Last_Rent = Last_Rent
    
    def __str__(self):
        return f"{self.Nickname}\n\nName: {self.Name}\nID: {self.ID}\nFunds: {self.Funds}\nDebt: {self.Debt}\nLast Rent: {self.Last_Rent}\nLast Review: {self.Reviews}"

class Vehicle:
    def __init__(self, Brand, Model, Color, HorsePower, Price_day, Available, 
                 Maintenance, Maintenance_Date, Service, Service_Date, Damage_Date, Damage, Incident_Date, Incident, Offer):
        self.Brand = Brand
        self.Model = Model
        self.Color = Color
        self.HorsePower = HorsePower
        self.Price_day = Price_day
        self.Available = Available

        self.Maintenance_Date = Maintenance_Date
        self.Maintenance = Maintenance
        self.Service_Date = Service_Date
        self.Service = Service
        self.Damage_Date = Damage_Date
        self.Damage = Damage
        self.Incident_Date = Incident_Date
        self.Incident = Incident
        self.Offer = Offer

    def Availability(self):
        return self.Available
        
    
    def __str__(self):
        return f"Brand: {self.Brand}\nModel: {self.Model}\nColor: {self.Color}\nHP: {self.HorsePower}HP\nPrice: R$ {self.Price_day}/day\nAvailability: {self.Available}\nLast Maintenance Record: {self.Maintenance_Date} {self.Maintenance}\nLast Service Record: {self.Service_Date} {self.Service}\nLast Damage Reported: {self.Damage_Date} {self.Damage}\nLast Incident Reported: {self.Incident_Date} {self.Incident}\nOffers: {self.Offer}"
