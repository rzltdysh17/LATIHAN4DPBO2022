from Airplane import Airplane
from Ship import Ship
from Driver import Driver

# Set Data Airplane
o_airplane = [Airplane() for i in range (5)]
o_airplane[0].setAirplane("Airbus A380-800", "Kerosene", 853, 4, "Commercial Aircraft", 80)
o_airplane[1].setAirplane("Boeing 747", "Kerosene", 467, 11, "Commercial Aircraft", 68)
o_airplane[2].setAirplane("A-10 Thunderbolt II", "Hydrogen", 2, 49, "Attack Aircraft", 17.42)
o_airplane[3].setAirplane("Lockheed Martin F-35 Lightning II", "Avtur", 2, 16, "Fighter Jet", 10.7)
o_airplane[4].setAirplane("Boeing B-52 Stratofortress", "Synthetic Fuel", 5, 69, "Strategic Bomber", 56.4)

# Print Data Airplane
print("=================================================================")
print("                          Airplane Data                          ")
print("=================================================================")
for i in range (5):
    o_airplane[i].printAirplane()

# Print Data Vehicle from Airplane
print("\n")
print("=================================================================")
print("                          Vehicle Data                           ")
print("=================================================================")
for i in range (5):
    o_airplane[i].printVehicle()
    print("=================================================================")

# Set Data Ship
o_ship = [Ship() for i in range (5)]
o_ship[0].setShip("Spectrum of the Seas", "Diesel", 4100, 3, "Cruise Ship", "Germany")
o_ship[1].setShip("USS Enterprise", "Deuterium", 5828, 61, "Aircraft Carrier", "United States")
o_ship[2].setShip("Iona", "Liquefied Natural Gas", 5200, 2, "Cruise Ship", "United Kingdom")
o_ship[3].setShip("KMS Bismarck", "Oil", 2200, 83, "Battleships", "Germany")
o_ship[4].setShip("Symphony of the Seas", "Diesel", 5400, 4, "Cruise Ship", "France")

# Print Data Ship
print("\n")
print("=================================================================")
print("                            Ship Data                            ")
print("=================================================================")
for i in range (5):
    o_ship[i].printShip()


# Print Data Vehicle from Airplane
print("\n")
print("=================================================================")
print("                          Vehicle Data                           ")
print("=================================================================")
for i in range (5):
    o_ship[i].printVehicle()
    print("=================================================================")

# Set Data Driver
o_driver = [Driver() for i in range (5)]
o_driver[0].setDriver(28675329, "Steven", "Male", 10974926, "Secret Agent", "Employee", 21849249, 2025, "Car")
o_driver[1].setDriver(29584029, "Katty", "Female", 76149124, "Mango Squash", "Marketing", 12768311, 2023, "Motorcycle")
o_driver[2].setDriver(89353203, "Jack", "Male", 76548376, "Secure Compagnie", "HRD", 67453298, 2027, "Car")
o_driver[3].setDriver(87265986, "Yunna", "Female", 98723456, "Universal", "Secretary", 76521974, 2024, "Motorcycle")
o_driver[4].setDriver(57129930, "Thonny", "Male", 86917253, "Friendly", "Driver", 86814984, 2025, "Bus")

# Print Data Driver
print("\n")
print("=================================================================")
print("                         Driver Data                             ")
print("=================================================================")
for i in range(5):
    o_driver[i].printDriver()

# Print Data Person from Driver
print("\n")
print("=================================================================")
print("                          Person Data                            ")
print("=================================================================")
for i in range(5):
    o_driver[i].printPerson()
    print("=================================================================")

# Print Data Job from Driver
print("\n")
print("=================================================================")
print("                           Job Data                              ")
print("=================================================================")
for i in range(5):
    o_driver[i].printJob()
    print("=================================================================")