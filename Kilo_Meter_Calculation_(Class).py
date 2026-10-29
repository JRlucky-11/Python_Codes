class Vehicle:
    def __init__(self, Brand_Name, Model_Name):
        self.Brand_Name = Brand_Name
        self.Model_Name = Model_Name
    
    def calculate_Remaining_Percentage(self, Distance):
        pass

class Petrol_Vehicle(Vehicle):
    def __init__(self, Brand_Name, Model_Name, Milage, Tank_Capacity):
        super().__init__(Brand_Name, Model_Name)
        self.Milage = Milage
        self.Tank_Capacity = Tank_Capacity

    def calculate_Remaining_Percentage(self, Distance):
        Fuel_Used = Distance / self.Milage
        Remaining_Fuel = self.Tank_Capacity - Fuel_Used

        if Remaining_Fuel < 0:
            print("\t\t-> [Sir Your Fuel is Low..!]")
            Remaining_Fuel = 0

        Remaining_Percentage = (Remaining_Fuel / self.Tank_Capacity) * 100
        print(f"\t\t> Sir, Your Fuel Used: {Fuel_Used:.2f}L | Remaining Fuel: {Remaining_Fuel:.2f}L -> ({Remaining_Percentage:.2f}%)")

class EV_Vehicle(Vehicle):
    def __init__(self, Brand_Name, Model_Name, Single_Charge_Range):
        super().__init__(Brand_Name, Model_Name)
        self.Single_Charge_Range = Single_Charge_Range
    
    def calculate_Remaining_Percentage(self, Distance):
        Battery_Used = (Distance / self.Single_Charge_Range) * 100
        Remaining_Battery = 100 - Battery_Used
        
        if Remaining_Battery < 0:
            print("\t\t-> [Sir Your Battery Low..!]")
            Remaining_Battery = 0
        
        # Remaining_Percentage = (Remaining_Battery / self.Single_Charge_Range) * 100
        print(f"\t\t> Sir, Battery Used: {Battery_Used:.2f}% | Remaining Battery: {Remaining_Battery:.2f}%")

def Trip_Details(Vehicle_Obj, Distance):
    print(f"\n\t--- Sir Your Trip Report Generated for {Vehicle_Obj.Brand_Name} {Vehicle_Obj.Model_Name} ---")
    Vehicle_Obj.calculate_Remaining_Percentage(Distance)
    

str1 = "[ Hello Sir, Welcome to Jarvis Style Vehicle Calculator ]"
print(str1.center(100, "-"))
print("1. Petrol Vehicle")
print("2. EV Vehicle")
print("")

while True:
    ch = input("> Sir, Please Select Your Vehicle: ")

    if ch == "1":
        brand = input("\t> Sir, Enter Your Brand Name: ")
        model = input("\t> Sir, Enter Your Model Name: ")
        mileage = float(input("\t> Sir, Enter Your Vehicle Mileage (Km/Litre): "))
        tank_cap = float(input("\t> Sir, Enter Tank Capacity (Litres): "))
        distance = float(input("\t> Sir, Enter Your Ridding Km: "))

        my_vehicle = Petrol_Vehicle(brand, model, mileage, tank_cap)
        Trip_Details(my_vehicle, distance)
        break

    elif ch == "2":
        brand = input("\t> Sir, Enter Your Brand Name: ")
        model = input("\t> Sir, Enter Your Model Name: ")
        full_range = float(input("\t> Sir, Full Charge Range (km): "))
        distance = float(input("\t> Sir, Enter Your Ridding Km: "))

        my_vehicle = EV_Vehicle(brand, model, full_range)
        Trip_Details(my_vehicle, distance)
        break

    else:
        print("> Sir, Please Enter Valid Choice...!")