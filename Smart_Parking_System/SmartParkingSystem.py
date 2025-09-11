# Smart Parking System:
# • Create classes Vehicle, ParkingSpot, and ParkingLot.
# • Create multiple objects (vehicles, spots, parking lot).
# • Demonstrate object creation, attribute initialization, and method calls.
# • Make sensitive attributes private (e.g., license plate, owner name, spot status).
# • Provide getter/setter methods to access/update them safely.
# • Show that direct access fails but methods work.
# • Vehicle is the base class.
# • Derived classes:
# Bike (extra attribute: helmet_required)
# Car (extra attribute: seats)
# SUV (extra attribute: four_wheel_drive)
# Truck (extra attribute: max_load_capacity)
# • Each child class overrides display() to print its own details.
# • Create a list of different vehicle objects (Bike, Car, SUV, Truck).
# • Iterate and call display() → each object responds differently.
# • Implement a calculate_parking_fee() method:
# Bike → ₹20/hour
# Car → ₹50/hour
# SUV → ₹70/hour
# Truck → ₹100/hour
# • Demonstrate runtime polymorphism by calling the method on different objects.
# • Create an abstract class/interface Payment (using abc module).
# • Define an abstract method process_payment(amount).
# • Create child classes:
# CashPayment
# CardPayment
# UPIPayment
# • Demonstrate abstraction by processing payments differently (just print “Paid ₹X via UPI”).
# Task 1: Vehicle Classes
# Implement base and derived vehicle classes with encapsulation.
# Override display() and calculate_parking_fee().
# Task 2: ParkingSpot Class
# Implement ParkingSpot with size restrictions (S, M, L, XL).
# Methods: assign_vehicle(), remove_vehicle().
# Ensure vehicle type fits correct spot size (Bike → S+, Car → M+, SUV → L+, Truck → XL only).
# Task 3: ParkingLot Class
# Store multiple parking spots.
# Methods:
# add_spot() → add new parking spots.
# show_spots() → display all spots and their status.
# park_vehicle(vehicle) → find suitable spot and park.
# unpark_vehicle(vehicle) → remove from spot and calculate fee.
# Task 4: Payment (Abstraction + Polymorphism)
# When un-parking a vehicle, calculate fee (based on hours).
# Ask user for payment method → process payment using appropriate child class.
# Task 5: Main Program
# Create a parking lot with mixed spots.
# Create multiple vehicle objects.
# Park/unpark vehicles.
# Demonstrate encapsulation, inheritance, polymorphism, and abstraction throughout.
from abc import ABC,abstractmethod
class Vehicle:
    def __init__(self,license_plate,owner_name,spot_status):
        self.__license_plate=license_plate
        self.__owner_name=owner_name
        self.__spot_status=spot_status

    def set_license_plate(self,license_plate):
        self.__license_plate=license_plate
    def get_license_plate(self):
        return self.__license_plate
        
    def set_owner_name(self,owner_name):
        self.__owner_name=owner_name
    def get_owner_name(self):
        return self.__owner_name
        
    def set_spot_status(self,spot_status):
        self.__spot_status=spot_status
    def get_spot_status(self):
        return self.__spot_status
    def display(self):
        print("Owner name",self.__owner_name)
        print("License number",self.__license_plate)
        print("Spot status",self.__spot_status)
    def calculate_parking_fee(self,hrs):
        return 0
class Bike(Vehicle):
    def __init__(self, license_plate, owner_name, spot_status,helmet_required):
        super().__init__(license_plate, owner_name, spot_status)
        self.helmet_required=helmet_required
    def display(self):
        print("Bike")
        print("Owner name",self.get_owner_name())
        print("License number",self.get_license_plate())
        print("Spot status",self.get_spot_status())
        print("helmet_required",self.helmet_required)
    def calculate_parking_fee(self,hrs):
            return 20*hrs
    

class Car(Vehicle):
    def __init__(self, license_plate, owner_name, spot_status,seats):
        super().__init__(license_plate, owner_name, spot_status)
        self.seats=seats
    def display(self):
        print("car")
        print("Owner name",self.get_owner_name())
        print("License number",self.get_license_plate())
        print("Spot status",self.get_spot_status())
        print("seats",self.seats)
    def calculate_parking_fee(self,hrs):
            return 50*hrs
    
class SUV(Vehicle):
    def __init__(self, license_plate, owner_name, spot_status,four_wheel_drive):
        super().__init__(license_plate, owner_name, spot_status)
        self.four_wheel_drive=four_wheel_drive
    def display(self):
        print("SUV")
        print("Owner name",self.get_owner_name())
        print("License number",self.get_license_plate())
        print("Spot status",self.get_spot_status())
        print("four_wheel drive",self.four_wheel_drive)
    def calculate_parking_fee(self,hrs):
            return 70*hrs
    

class Truck(Vehicle):
    def __init__(self, license_plate, owner_name, spot_status,max_load_capacity):
        super().__init__(license_plate, owner_name, spot_status)
        self.max_load_capacity=max_load_capacity
    def display(self):
        print("Truck")
        print("Owner name",self.get_owner_name())
        print("License number",self.get_license_plate())
        print("Spot status",self.get_spot_status())
        print("max load capacity",self.max_load_capacity)
    def calculate_parking_fee(self,hrs):
            return 100*hrs
class Payment:
    @abstractmethod
    def process_payement(self):
        pass
class CashPayment(Payment):
    def process_payement(self,amount):
        print(f"Paid {amount} in cash")
class CardPayment(Payment):
    def process_payement(self,amount):
        print(f"Paid {amount} using credit/debit card")
class UPIPayment(Payment):
    def process_payement(self,amount):
        print(f"Paid {amount}using UPI")
# v1=Bike("a1819","ram","not parked","yes")
# v2=Car("a67f5","raju","yes",4)
# v3=SUV("7gSUV","ravi","no",four_wheel_drive="Yes")
# v4=Truck("76g456","sheela","yes",max_load_capacity="25 tonns")
class ParkingSpot:
    def __init__(self, spot_id, size):
        self.spot_id = spot_id      
        self.size = size            
        self.__occupied = False     
        self.vehicle = None 
    def assign_vehicle(self, vehicle):
        if self.__occupied:
           return False
        allowed_sizes={
            Bike:["S","M","L","XL"]
            ,Car:["M","L","XL"],
            SUV:["L","XL"],
            Truck:["XL"]
        }
        for v_type,size in allowed_sizes.items():
            if isinstance(vehicle,v_type) and self.size in allowed_sizes:
                self.vehicle=vehicle
                self.__occupied=True
                vehicle.set_spot_status("Parked")
                return True
        return False
    def remove_vehicle(self,vehicle):
        if not self.__occupied:
            return None
        self.vehicle.set_spot_status("Not Parked")
        removed_vehicle=self.vehicle
        self.vehicle=None
        self.__occupied=False
        return removed_vehicle
    def show_status(self):
        if self.__occupied:
            return f"Spot {self.spot_id} ({self.size})- occupied by{self.vehicle.get_license_plate()}"
        else:
            return f"Spot {self.spot_id}({self.size})- Free"
        
class ParkingLot:
    def __init__(self,name):
        self.spots = []
        self.name=name

    def add_spot(self, spot):
        self.spots.append(spot)
        print(f"Added spot{spot.spot_id}({spot.size}) to {self.name}")

    def show_spots(self):
        print("Parking Spots")
        for spot in self.spots:
            print(spot.show_status())

    def park_vehicle(self,vehicle):
        for spot in self.spots:
            if spot.assign_vehicle(vehicle):
                print(f"Vehicle {vehicle.get_license_plate()} parked in Spot {spot.spot_id}")
                return True
        print(f"No spot found for {vehicle.get_license_plate()}")
        return False

    def unpark_vehicle(self, vehicle, hrs):
        for spot in self.spots:
            if spot.vehicle == vehicle:
                fee, removed_vehicle = spot.remove_vehicle(hrs)
                print(f"Vehicle {removed_vehicle.get_license_plate()} is unparked.Fee-{fee}")
                return fee
        print(f"Vehicle {vehicle.get_license_plate()} not found in the parking lot")
        return None
bike1 = Bike("B101", "TS01AB1234", "Rahul", True)
car1 = Car("C201", "TS05CD5678", "Priya", 5)
suv1 = SUV("S301", "TS09EF9012", "Anjali", True)
truck1 = Truck("T401", "TS11XY4455", "Ravi", 12)
li=[bike1,car1,suv1,truck1]
for i in li:
    i.display()
    print("Parking fee",i.calculate_parking_fee(10))
lot = ParkingLot("CityMall Parking")
# Add spots of different sizeslot.add_spot(ParkingSpot(1, "S"))
lot.add_spot(ParkingSpot(2, "M"))
lot.add_spot(ParkingSpot(3, "M"))
lot.add_spot(ParkingSpot(4, "L"))
lot.add_spot(ParkingSpot(5, "XL"))
lot.park_vehicle(bike1)
lot.unpark_vehicle(car1, hrs=3)
lot.show_spots()       
        

