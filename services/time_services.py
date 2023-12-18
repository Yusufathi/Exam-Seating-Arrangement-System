import time
from datetime import datetime


def get_date_time_str():
    return time.time()

def getDate():
    current_date = datetime.now().strftime('%Y-%m-%d')
    return current_date