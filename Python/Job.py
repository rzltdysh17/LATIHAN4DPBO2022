# Kelas Job Parent Class dari Kelas Driver
class Job:
    # Atribut Private
    __nip = 0
    __companyName = ""
    __position = ""
     
    # Constructor
    def __init__(self):
        self.__nip = 0
        self.__companyName = ""
        self.__position = ""
    
    # Metode Setter
    def setNip(self, nip):
        self.__nip = nip

    def setCompanyName(self, companyName):
        self.__companyName = companyName

    def setPosition(self, position):
        self.__position = position
    
    def setJob(self, nip, companyName, position):
        self.setNip(nip)
        self.setCompanyName(companyName)
        self.setPosition(position)
    
    # Metode Getter
    def getNip(self):
        return self.__nip

    def getCompanyName(self):
        return self.__companyName

    def getPosition(self):
        return self.__position

    # Metode Print Data
    def printJob(self):
        print("NIP          : " + str(self.getNip()))
        print("Company Name : " + self.getCompanyName())
        print("Position     : " + self.getPosition())