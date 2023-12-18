from services.registeration_service import RegisterationService
from services.schedule_service import ScheduleService
from views.seating_view import SeatingView
from views.ranges_view import RangesView

if __name__ == "__main__":
    inputScheduleCSVPath = '.\input\input_after_preproccessing.csv'
    scheduleService = ScheduleService(inputFilePath=inputScheduleCSVPath)
    schedule = scheduleService.getModel().scheduleObj
    daysCount = len(schedule.items())

    for date, time_slots in schedule.items():
        for time, exams in time_slots.items():
            for exam in exams:
                examRoom = exam['Room(s)']
                courseName = exam['Course Name']
                courseCode = exam['Course Code']
                noOfStudents = exam['No. of Students']
                examDate = date.split("_")[0]
                examDay = date.split("_")[1]
                examTime = time
                print(f"    Room(s): {examRoom}")
                print(f"    No. Of Students: {noOfStudents}")
                print(f"    Course Name: {courseName}")
                print(f"    Course Code: {courseCode}")
                print(f"    Exam Date: {examDate}")
                print(f"    Exam Day: {examDay}")
                print(f"    Exam Time: {examTime}")
                print("==========================================")
                
               

        
    




    # reService = RegisterationService()
    # registerationModel = reService.getModel()
    # inputScheduleCSVPath = '.\input\input_after_preproccessing.csv'
    # scheduleService = ScheduleService(inputFilePath=inputScheduleCSVPath)
    # sv = SeatingView()
    # rv = RangesView()
    