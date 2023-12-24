from services.registeration_service import RegisterationService
from services.schedule_service import ScheduleService
from views.seating_view import SeatingView
from views.ranges_view import RangesView
import json
registerationObj = {}
rangesObj = {}


def buildRoomsLists(examRoom, courseName, courseCode, noOfStudents, examDate, examDay, examTime):
    try:
        courseCode = courseCode.replace(" ", "")
        courseName = courseName.strip()
        startID = registerationObj[courseCode][0][0]
        endID = registerationObj[courseCode][noOfStudents - 1][0]
        examList = [['Seating#', 'ID', 'Name', 'Signature']]
        for i in range(noOfStudents):
            studentRecord = []
            studentID = registerationObj[courseCode][i][0]
            studentName = registerationObj[courseCode][i][1]
            studentRecord.append(i+1)
            studentRecord.append(studentID)
            studentRecord.append(studentName)
            studentRecord.append('             ')
            examList.append(studentRecord)
        for i in range(noOfStudents):
            del registerationObj[courseCode][0]

        SeatingView(courseName, courseCode, examDate,
                    examTime, examRoom, examList)
        roomRecord = [examRoom, startID, endID, noOfStudents]
        addExamRange(courseName, courseCode, roomRecord)

    except:
        print("Something Went wrong. Please make sure that the data in the schedule is preprocessed and there is no spaces. \n Also Please make sure that the count of students in the course is synced with the count of students in the registeration DB. ")


def buildExamRanges():
    file_path = "./json/ranges.json"
    with open(file_path, "w") as json_file:
        json.dump(rangesObj, json_file)

    print(f"The Ranges has been written to {file_path}")

    for course_code, course_info in rangesObj.items():
        name = course_info['name']
        list = course_info['list']
        RangesView(name, course_code, list)


def addExamRange(courseName, courseCode, roomRecord):
    if courseCode not in rangesObj:
        rangesObj[courseCode] = {}
        rangesObj[courseCode]["name"] = courseName
        rangesObj[courseCode]["index"] = 1
        rangesObj[courseCode]["list"] = [
            ['index#', 'Room', 'Start ID', 'End ID', 'Capacity']]

    roomRecord = [rangesObj[courseCode]["index"]] + roomRecord
    rangesObj[courseCode]["list"].append(roomRecord)
    rangesObj[courseCode]["index"] = rangesObj[courseCode]["index"] + 1


def iterateOverScheduleAndGenerateExamList():
    inputScheduleCSVPath = '.\input\input_after_preproccessing - backup.csv'
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
                buildRoomsLists(examRoom, courseName, courseCode,
                                noOfStudents, examDate, examDay, examTime)


if __name__ == "__main__":
    reService = RegisterationService()
    registerationObj = reService.getModel().subjectsStudentsLists
    iterateOverScheduleAndGenerateExamList()
    buildExamRanges()
