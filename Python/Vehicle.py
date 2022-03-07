# Kelas Vehicle Parent Class dari Kelas Airplane dan Ship
class Vehicle:
    # Atribut Private
    __name = ""
    __fuelType = ""
    __maxPassengers = 0

    # Constructor
    def __init__(self):
        self.__name = ""
        self.__fuelType = ""
        self.__maxPassengers = 0
    
    # Metode Setter
    def setName(self, name):
        self.__name = name

    def setFuelType(self, fuelType):
        self.__fuelType = fuelType

    def setMaxPassengers(self, maxPassengers):
        self.__maxPassengers = maxPassengers

    def setVehicle(self, name, fuelType, maxPassengers):
        self.setName(name)
        self.setFuelType(fuelType)
        self.setMaxPassengers(maxPassengers)
    
    # Metode Getter
    def getName(self):
        return self.__name

    def getFuelType(self):
        return self.__fuelType
    
    def getMaxPassengers(self):
        return self.__maxPassengers
    
    # Metode Print Move
    def move(self, isMove):
        if isMove is True:
            print(self.getName() + " is moving.")
        else:
            print(self.getName() + " isn't moving.")

    # Metode Print Data
    def printVehicle(self):
        print("Name                     : " + self.getName())
        print("Fuel Type                : " + self.getFuelType())
        print("Max Passenger            : " + str(self.getMaxPassengers()) + " Passengers")