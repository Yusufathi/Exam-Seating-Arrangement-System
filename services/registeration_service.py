import requests
from services.time_services import get_date_time_str
from models.registeration_model import RegisterationModel
import csv

domain = "http://ec2-54-147-218-160.compute-1.amazonaws.com:8181"
end_point = "/get_registertions/csv"
ignored_courses_names_list = ["Project II", "Project I",
                              "English Language 101", "English Language 102",
                              "English Language 100", "Practical Applications in Computer Science II"]
ignored_courses_codes_list = []


class RegisterationService:
    __localFilePath = None
    __registeration = None

    def __init__(self):
        self.getDataFromRegisterationSite()
        self.__registeration = RegisterationModel()
        self.convertCSVToModel()
        self.__registeration.createJsonFile()

    def getDataFromRegisterationSite(self):
        print(f"Calling Endpoint : {domain+end_point}")
        response = requests.get(domain+end_point)
        res = None
        if response.status_code == 200:
            self.__localFilePath = f"./data/{
                get_date_time_str()}_registeration.csv"
            with open(self.__localFilePath, 'wb') as file:
                file.write(response.content)
            print(
                f"CSV file downloaded successfully to: {self.__localFilePath}")
            res = True
        else:
            print(
                f"Failed to download CSV file. Status code: {response.status_code}")
            res = False
        return res

    def convertCSVToModel(self):
        registerationCount = 1
        with open(self.__localFilePath, 'r', encoding="utf8") as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                registerationCount += 1
                code = row['subject_code']
                subject_name = row['subject_name']
                name = self.getFirst3Names(row['student_name'])
                id = row['student_id']
                if any(subject_name in x for x in ignored_courses_names_list) or any(code in y for y in ignored_courses_codes_list):
                    continue
                try:
                    type(
                        self.__registeration.subjectsStudentsLists[code])
                except:
                    self.__registeration.subjectsStudentsLists[code] = [
                    ]

                self.__registeration.subjectsStudentsLists[code].append(
                    (id, name))

        self.__registeration.totalRegisterationCount = registerationCount
        self.__registeration.subjectsCount = len(
            self.__registeration.subjectsStudentsLists)

    def getModel(self):
        return self.__registeration

    def getFirst3Names(self, full_name):
        names = full_name.split()
        return ' '.join(names[:3])
