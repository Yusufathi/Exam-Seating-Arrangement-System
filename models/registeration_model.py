class RegisterationModel :
    subjectsCount = 0
    totalStudentsCount = 0
    totalRegisterationCount = 0
    subjectsStudentsLists = {}


    
    def __str__(self):
        return self.subjectsCount + " " + self.totalStudentsCount + " " + self.totalRegisterationCount +" " + self.subjectsStudentsLists