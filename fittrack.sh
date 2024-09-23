#!/bin/bash

# Create User
create_user() {
    PYTHONPATH=. python fittrack/cli.py create-user --name "$1" --age "$2" --height "$3" --weight "$4" --fitness-level "$5"
}

# Delete User
delete_user() {
    PYTHONPATH=. python fittrack/cli.py delete-user --user-id "$1"
}

# Set Physical Goal
set_goal() {
    PYTHONPATH=. python fittrack/cli.py set-physical-goal --user-id "$1" --goal "$2"
}

# Log Workout
log_workout() {
    echo "Debug: Logging workout with user ID: $1, exercise: $2, duration: $3, calories burned: $4"
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

# Command handling
case "$1" in
    create_user)
        create_user "$2" "$3" "$4" "$5" "$6"
        ;;
    delete_user)
        delete_user "$2"
        ;;
    set_goal)
        set_goal "$2" "$3"
        ;;
    log_workout)
        log_workout "$2" "$3" "$4" "$5"
        ;;
    log_nutrition)
        log_nutrition "$2" "$3" "$4"
        ;;
    journal_mental_health)
        journal_mental_health "$2" "$3"
        ;;
    calculate_bmi)
        calculate_bmi "$2"
        ;;
    *)
        echo "Invalid command"
        echo "Usage: $0 {create_user|delete_user|set_goal|log_workout|log_nutrition|journal_mental_health|calculate_bmi} ..."
        exit 1
        ;;
esac
