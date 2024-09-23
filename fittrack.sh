#!/bin/bash

# Function to create a user
create_user() {
    if PYTHONPATH=. python fittrack/cli.py create-user --name "$1" --age "$2" --height "$3" --weight "$4" --fitness-level "$5"; then
        echo "User '$1' created successfully."
    else
        echo "Error creating user '$1'."
    fi
}

# Function to update a user
update_user() {
    if PYTHONPATH=. python fittrack/cli.py update-user --user-id "$1" --name "$2" --age "$3" --height "$4" --weight "$5" --fitness-level "$6"; then
        echo "User with ID $1 updated successfully."
    else
        echo "Error updating user with ID $1."
    fi
}

# Function to delete a user
delete_user() {
    if PYTHONPATH=. python fittrack/cli.py delete-user --user-id "$1"; then
        echo "User with ID $1 deleted successfully."
    else
        echo "Error deleting user with ID $1."
    fi
}

# Function to log nutrition
log_nutrition() {
    if PYTHONPATH=. python fittrack/cli.py log-nutrition --user-id "$1" --meal "$2" --calories "$3"; then
        echo "Nutrition logged successfully for user $1: $2, $3 calories."
    else
        echo "Error logging nutrition for user $1."
    fi
}

# Function to log workout
log_workout() {
    if PYTHONPATH=. python fittrack/cli.py log-workout --user-id "$1" --exercise "$2" --duration "$3" --calories-burned "$4"; then
        echo "Workout logged successfully for user $1: $2 for $3 minutes, burning $4 calories."
    else
        echo "Error logging workout for user $1."
    fi
}

# Function to journal mental health
# Function to journal mental health
journal_mental_health() {
    PYTHONPATH=. python fittrack/cli.py journal-mental-health --user-id "$1" --entry "$2"
    echo "Mental health journal entry saved for user $1: '$2'."
}


# Function to calculate BMI
calculate_bmi() {
    if PYTHONPATH=. python fittrack/cli.py calculate-bmi --user-id "$1"; then
        echo "BMI calculated for user $1."
    else
        echo "Error calculating BMI for user $1."
    fi
}

# Main menu and command handling
case "$1" in
    create_user)
        create_user "$2" "$3" "$4" "$5" "$6"
        ;;
    update_user)
        update_user "$2" "$3" "$4" "$5" "$6" "$7"
        ;;
    delete_user)
        delete_user "$2"
        ;;
    log_nutrition)
        log_nutrition "$2" "$3" "$4"
        ;;
    log_workout)
        log_workout "$2" "$3" "$4" "$5"
        ;;
    journal_mental_health)
        journal_mental_health "$2" "$3"
        ;;
    calculate_bmi)
        calculate_bmi "$2"
        ;;
    *)
        echo "Invalid command"
        echo "Usage: $0 {create_user|update_user|delete_user|log_nutrition|log_workout|journal_mental_health|calculate_bmi}"
        exit 1
        ;;
esac
