from PythonProject.iteration1.main.repositories.abstarct.AbstarctStudentRepository import AbstactRepository
from collections import OrderedDict

class StudentRepository(AbstactRepository):
    def __init__(self,rawRepo):
        self.studentRawRepo = rawRepo
    def createRepoByUniqueID(self,setofElements,nameOfUniqueElement):
        tempRepo = OrderedDict()
        for i in setofElements:
            if(getattr(i,nameOfUniqueElement) in tempRepo):
                continue
            else:
                tempRepo[i.getNumber()] = i
        print(tempRepo)
        return tempRepo
