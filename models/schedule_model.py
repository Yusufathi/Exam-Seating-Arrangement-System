import json
from services.time_services import get_date_time_str


class ScheduleModel:
    scheduleObj = []

    def __init__(self):
        pass

    def createJsonFile(self, path='./json'):
        path = path + f"/{get_date_time_str()}_schedule.json"
        with open(path, 'w', encoding='utf-8-sig') as json_file:
            json.dump(self.scheduleObj, json_file, indent=2, ensure_ascii=False)
            print(f"JSON data has been written to: {path}")
