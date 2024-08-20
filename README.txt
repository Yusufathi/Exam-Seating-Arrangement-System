# Exam Seating Arrangement System

This project is a Python-based system designed to automate the process of generating seating arrangements for exams based on registration and scheduling data. It creates detailed PDF reports for exam seating and room ranges, ensuring efficient organization and management of exam sessions.

## Features

- **Automated Data Processing**: 
  - Fetch registration data from a remote server.
  - Parse scheduling CSV files.
  - Automatically generate JSON files for both registration and schedule data.

- **PDF Report Generation**:
  - Generate PDFs for seating arrangements based on the exam room, course code, and student list.
  - Create room range reports showing the start and end ID for students in each exam room.

- **Error Handling**:
  - Identifies and logs errors, such as mismatched student counts between registration and schedule files.

## Project Structure

- `main.py`: The entry point of the system, which orchestrates the entire process from fetching data to generating reports.
  
- `models/`: Contains data models for handling registration and scheduling data.
  - `registeration_model.py`: Manages the registration data, including students' details and course registrations.
  - `schedule_model.py`: Handles scheduling data, including dates, times, and room assignments.
  
- `services/`: Includes service classes that provide functionalities to convert CSV files into models and interact with external systems.
  - `registeration_service.py`: Handles fetching and processing registration data.
  - `schedule_service.py`: Converts the scheduling CSV into structured data for further processing.
  - `time_services.py`: Utility functions for date and time operations.
  
- `views/`: Responsible for generating the final PDF reports.
  - `seating_view.py`: Creates seating arrangement PDFs for each exam room.
  - `ranges_view.py`: Generates PDFs showing the ranges of student IDs in each room.

- `input/`: Directory where the input CSV files for scheduling are stored.

- `outputs/`: Directory where the generated JSON files and PDF reports are saved.

## Input CSV Structure

The system expects specific formats for the input CSV files for scheduling. Below is a sample of what the scheduling file should look like:

### Schedule CSV

| Date       | Day      | Time     | Room(s)   | Course Code | Course Name                   | No. of Students |
|------------|----------|----------|-----------|-------------|-------------------------------|-----------------|
| 2024-08-20 | Tuesday  | 09:00 AM | Room 101  | CSC201      | Fundamentals of Programming II | 40              |
| 2024-08-20 | Tuesday  | 11:00 AM | Room 102  | CSC202      | Data Structures               | 35              |
| 2024-08-21 | Wednesday| 09:00 AM | Room 103  | CSC203      | Operating Systems             | 30              |

Ensure that your input CSV files follow this structure closely to ensure proper processing by the system.

## How to Use

1. **Install Dependencies**:
   Ensure you have all the necessary Python libraries installed. You can install the dependencies using pip:
   ```bash
   pip install -r requirements.txt

Prepare Input Files:

Place your scheduling CSV file in the input/ directory.
Ensure that the registration endpoint is correctly configured in registeration_service.py.
Run the Program:
Execute the main.py file to generate the seating arrangements and room ranges:

bash
Copy code
python main.py
Review Outputs:

The generated PDFs and any remaining data will be saved in the outputs/ directory.
If any registrations were not processed due to mismatches, a left.json file will be created in the outputs directory.
Example Output
Seating Arrangement PDF: A detailed PDF for each exam room listing students, their IDs, and designated seats.
Room Ranges PDF: A summary PDF showing the range of student IDs in each room.
Contributing
Contributions are welcome! Please create an issue or pull request for any improvements or bug fixes.

License
This project is licensed under the MIT License. See the LICENSE file for details.