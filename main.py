from services.registeration_service import RegisterationService
from services.schedule_service import ScheduleService


if __name__ == "__main__":
    # reService = RegisterationService()
    # registerationModel = reService.getModel()
    
    inputScheduleCSVPath = '.\input\input_after_preproccessing.csv'
    scheduleService = ScheduleService(inputFilePath=inputScheduleCSVPath)
