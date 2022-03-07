from Vehicle import Vehicle

# Kelas Airplane Child Class dari Kelas Vehicle
class Airplane(Vehicle):
    # Atribut Private
    __age = 0
    __type = ""
    __wingsLength = 0

    # Constructor
    def __init__(self):
        self.__age = 0
        self.__type = ""
        self.__wingsLength = 0
    
    # Metode Setter
    def setAge(self, age):
        self.__age = age

    def setType(self, type):
        self.__type = type

    def setWingsLength(self, wingsLength):
        self.__wingsLength = wingsLength
    
    def setAirplane(self, name, fuelType, maxPassengers, age, type, wingsLength):
        self.setVehicle(name, fuelType, maxPassengers)
        self.setAge(age)
        self.setType(type)
        self.setWingsLength(wingsLength)
    
    # Metode Getter
    def getAge(self):
        return self.__age

    def getType(self):
        return self.__type
    
    def getWingsLength(self):
        return self.__wingsLength

    # Metode Print Data
    def printAirplane(self):
        self.printVehicle()
        print("Age                      : " + str(self.getAge()) + " Years")
        print("Type                     : " + self.getType())
        print("Wings Length             : " + str(self.getWingsLength()) + " Meters")
        self.move(True)
        print("=================================================================")