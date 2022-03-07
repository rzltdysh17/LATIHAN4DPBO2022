# Kelas Person Parent Class dari Kelas Driver
class Person:    
    # Atribut Private
    __nik = 0
    __name = ""
    __gender = ""

    # Constructor
    def __init__(self):
        self.__nik = 0
        self.__name = ""
        self.__gender = ""
    
    # Metode Setter
    def setNik(self, nik):
        self.__nik = nik

    def setName(self, name):
        self.__name = name

    def setGender(self, gender):
        self.__gender = gender
    
    def setPerson(self, nik, name, gender):
        self.setNik(nik)
        self.setName(name)
        self.setGender(gender)
    
    # Metode Getter
    def getNik(self):
        return self.__nik

    def getName(self):
        return self.__name

    def getGender(self):
        return self.__gender
    
    # Metode Print Sleep
    def sleep(self, isSleep):
        if isSleep is True:
            print(self.getName() + " is sleeping.")
        else:
            print(self.getName() + " isn't sleeping.")

    # Metode Print Data
    def printPerson(self):
        print("NIK          : " + str(self.getNik()))
        print("Name         : " + self.getName())
        print("Gender       : " + self.getGender())