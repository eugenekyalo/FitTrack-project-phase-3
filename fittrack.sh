#!/bin/bash

# Create User
create_user() {
    PYTHONPATH=. python fittrack/cli.py create-user --name "$1" --age "$2" --height "$3" --weight "$4" --fitness-level "$5"
}

# Set Physical Goal
set_goal() {
    PYTHONPATH=. python fittrack/cli.py set-physical-goal --user-id "$1" --goal "$2"
}

# Log Workout
log_workout() {
    PYTHONPATH=. python fittrack/cli.py log-workout --user-id "$1" --exercise "$2" --duration "$3" --calories-burned "$4"
}

# Log Nutrition
log_nutrition() {
    PYTHONPATH=. python fittrack/cli.py log-nutrition --user-id "$1" --meal "$2" --calories "$3"
}

# Journal Mental Health
journal_mental_health() {
    PYTHONPATH=. python fittrack/cli.py journal-mental-health --user-id "$1" --entry "$2"
}

# Calculate BMI
calculate_bmi() {
    PYTHONPATH=. python fittrack/cli.py calculate-bmi --user-id "$1"
}
