import json
from services.time_services import get_date_time_str

class RegisterationModel :
    subjectsCount = 0
    totalRegisterationCount = 0
    subjectsStudentsLists = {}

    def createJsonFile(self,path='./json'):
        obj = self.subjectsStudentsLists
        obj['subjectsCount'] = self.subjectsCount
        obj['totalRegisterationCount'] = self.totalRegisterationCount
        path = path + f"/{get_date_time_str()}_registeration.json"

        with open(path, 'w') as json_file:
            json.dump(obj, json_file, indent=2)
            print(f"JSON data has been written to: {path}")