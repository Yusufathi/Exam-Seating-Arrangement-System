from models.schedule_model import ScheduleModel
import csv
from collections import defaultdict


class ScheduleService:
    __localFilePath = None
    __schedule = None

    def __init__(self, inputFilePath="/input/input.csv"):
        self.__localFilePath = inputFilePath
        self.__schedule = ScheduleModel()
        self.convertCSVToModel()

    def convertCSVToModel(self):
        structured_data = defaultdict(lambda: defaultdict(list))

        with open(self.__localFilePath, 'r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                day = row['Date']+"_"+row['Day'].replace(" ", "")
                time = row['Time'].replace(" ", "")
                row_data = {
                    'Date': row['Date'],
                    'Level': row['Level'],
                    'Course Code': row['Course Code'],
                    'Course Name': row['Course Name'],
                    'Instructor': row['Instructor'],
                    'No. of Students': int(row['No. of Students']),
                    'Required No. of Proctors': int(row['Required No. of Proctors']),
                    'Room(s)': row['Room(s)'],
                    'No. of Students/ Room': int(row['No. of Students/ Room']),
                    'No. of proctors / Room': int(row['No. of proctors / Room']),
                    'Proctor(s)': row['Proctor(s)']
                }
                structured_data[day][time].append(row_data)

        self.__schedule.scheduleObj = structured_data
        self.__schedule.createJsonFile()

    def getModel(self):
        return self.__schedule
