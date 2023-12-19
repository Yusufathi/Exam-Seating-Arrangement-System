from services.registeration_service import RegisterationService
from services.schedule_service import ScheduleService
from views.seating_view import SeatingView
from views.ranges_view import RangesView

registerationObj = {}
rangesObj = {}

def buildRoomsLists(examRoom, courseName, courseCode, noOfStudents, examDate, examDay, examTime):
    courseCode = courseCode.replace(" ","")
    startID = registerationObj[courseCode][0][0]
    endID = registerationObj[courseCode][noOfStudents - 1][0]
    # print(courseCode,courseName,startID,endID)
    for i in range(noOfStudents):
        print(registerationObj[courseCode][i])
        

    # print(f"    Room(s): {examRoom}")
    # print(f"    No. Of Students: {noOfStudents}")
    # print(f"    Course Name: {courseName}")
    # print(f"    Course Code: {courseCode}")
    # print(f"    Exam Date: {examDate}")
    # print(f"    Exam Day: {examDay}")
    # print(f"    Exam Time: {examTime}")
    # print("==========================================")

def buildExamRange():
    # sv = SeatingView()
    # rv = RangesView()
    pass


def iterateOverExamRooms():
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
                buildRoomsLists(examRoom,courseName,courseCode,noOfStudents,examDate,examDay,examTime)
                


if __name__ == "__main__":
    reService = RegisterationService()
    registerationObj = reService.getModel().subjectsStudentsLists
    iterateOverExamRooms()