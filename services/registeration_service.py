import requests
from services.time_services import get_date_time_str

domain = "http://ec2-54-147-218-160.compute-1.amazonaws.com:8181"
end_point = "/get_registertions/csv"

class RegisterationService :

    def get_Data(self):
        response = requests.get(domain+end_point)
        print(domain+end_point)
        if response.status_code == 200:
            local_file_path = f"./data/{get_date_time_str()}_registeration.csv"
            print(local_file_path)

            with open(local_file_path, 'wb') as file:
                file.write(response.content)

            print(f"CSV file downloaded successfully to: {local_file_path}")
        else:
            print(f"Failed to download CSV file. Status code: {response.status_code}")
