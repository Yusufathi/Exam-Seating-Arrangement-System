import requests
from services.time_services import get_date_time_str

domain = "http://ec2-54-147-218-160.compute-1.amazonaws.com:8181"
end_point = "/get_registertions/csv"

class RegisterationService :
    _localFilePath = None
    def __init__(self):
        self.getDataFromRegisterationSite()

    def getDataFromRegisterationSite(self):
        print(f"Calling Endpoint : {domain+end_point}")
        response = requests.get(domain+end_point)
        res = None
        if response.status_code == 200:
            _localFilePath = f"./data/{get_date_time_str()}_registeration.csv"
            with open(_localFilePath, 'wb') as file:
                file.write(response.content)
            print(f"CSV file downloaded successfully to: {_localFilePath}")
            res = True
        else:
            print(f"Failed to download CSV file. Status code: {response.status_code}")
            res = False
        return res

    def convertRowDataToModel(self):
        pass