FitTrack - Comprehensive Health and Wellness Platform
Overview
FitTrack is a Command Line Interface (CLI) application designed to track both physical and mental health, providing a comprehensive health and wellness platform. The application allows users to monitor their physical goals, mental health, workout routines, and nutrition. It is built using Python and SQLite, ensuring simplicity and ease of use.

Features
Physical Health Tracking: Track weight, height, and fitness goals.
Mental Health Tracking: Journal mental wellness and set mental health goals.
Workout Logging: Record workouts and set fitness goals.
Nutrition Logging: Track daily food intake and calories.
BMI and Calorie Calculations: Calculate Body Mass Index (BMI) and daily calorie needs.
Installation
Clone the Repository

bash
Copy code
git clone https://github.com/eugenekyalo/phase-3-project-FitTrack-Comprehensive-Health-and-Wellness-Platform.git
Navigate to the Project Directory

bash
Copy code
cd FitTrack-project-phase-3
Set Up a Virtual Environment

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Initialize the Database

bash
Copy code
python fittrack/cli.py --init-db
Usage
Create a New User

bash
Copy code
python fittrack/cli.py --create-user --name "John Doe" --age 30 --height 180 --weight 75 --fitness-level "Intermediate"
Set Physical Goals

bash
Copy code
python fittrack/cli.py --set-physical-goal --user-id 1 --goal "Lose 5 kg"
Log a Workout

bash
Copy code
python fittrack/cli.py --log-workout --user-id 1 --exercise "Running" --duration 30 --calories-burned 300
Track Nutrition

bash
Copy code
python fittrack/cli.py --log-nutrition --user-id 1 --meal "Lunch" --calories 600
Journal Mental Health

bash
Copy code
python fittrack/cli.py --journal-mental-health --user-id 1 --entry "Feeling great today!"
Calculate BMI

bash
Copy code
python fittrack/cli.py --calculate-bmi --user-id 1
Testing
To ensure the application is functioning as expected, run the test suite:

bash
Copy code
pytest
Project Structure
markdown
Copy code
FitTrack-project-phase-3/
├── fittrack/
│   ├── __init__.py
│   ├── cli.py
│   ├── models.py
│   └── ...
├── tests/
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_cli.py
│   └── ...
├── pytest.ini
├── main.py
├── requirements.txt
└── README.md
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with any improvements or bug fixes.

License
This project is licensed under the MIT License. See the LICENSE file for details.