from Person import Person
from Job import Job

# Kelas Driver Child Class dari Kelas Person dan Job
class Driver(Person, Job):
    # Atribut Private
    __licenseID = 0
    __activeUntil = 0
    __vehicleType = ""

    # Constructor
    def __init__(self):
        self.__licenseID = 0
        self.__activeUntil = 0
        self.__vehicleType = ""
    
    # Metode Setter
    def setLicenseID(self, licenseID):
        self.__licenseID = licenseID

    def setActiveUntil(self, activeUntil):
        self.__activeUntil = activeUntil

    def setVehicleType(self, vehicleType):
        self.__vehicleType = vehicleType
    
    def setDriver(self, nik, name, gender, nip, companyName, position, licenseID, activeUntil, vehicleType):
        self.setPerson(nik, name, gender)
        self.setJob(nip, companyName, position)
        self.setLicenseID(licenseID)
        self.setActiveUntil(activeUntil)
        self.setVehicleType(vehicleType)
    
    # Metode Getter
    def getLicenseID(self):
        return self.__licenseID

    def getActiveUntil(self):
        return self.__activeUntil

    def getVehicleType(self):
        return self.__vehicleType

    # Metode Print Data
    def printDriver(self):
        self.printPerson()
        self.printJob()
        print("License ID   : " + str(self.getLicenseID()))
        print("Active Until : " + str(self.getActiveUntil()))
        print("Vehicle Type : " + self.getVehicleType())
        self.sleep(True)
        print("=================================================================")