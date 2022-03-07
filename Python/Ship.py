from calendar import c
from Vehicle import Vehicle

# Kelas Ship Child Class dari Kelas Vehicle
class Ship(Vehicle):
    # Atribut Private
    __age = 0
    __type = ""
    __countryOfManufacture = ""

    # Constructor
    def __init__(self):
        self.__age = 0
        self.__type = ""
        self.__countryOfManufacture = ""
    
    # Metode Setter
    def setAge(self, age):
        self.__age = age

    def setType(self, type):
        self.__type = type

    def setCountryOfManufacture(self, countryOfManufacture):
        self.__countryOfManufacture = countryOfManufacture
    
    def setShip(self, name, fuelType, maxPassengers, age, type, countryOfManufacture):
        self.setVehicle(name, fuelType, maxPassengers)
        self.setAge(age)
        self.setType(type)
        self.setCountryOfManufacture(countryOfManufacture)
    
    # Metode Getter
    def getAge(self):
        return self.__age

    def getType(self):
        return self.__type
    
    def getCountryOfManufacture(self):
        return self.__countryOfManufacture

    # Metode Print Data
    def printShip(self):
        self.printVehicle()
        print("Age                      : " + str(self.getAge()) + " Years")
        print("Type                     : " + self.getType())
        print("Country of Manufacture   : " + self.getCountryOfManufacture())
        self.move(False)
        print("=================================================================")