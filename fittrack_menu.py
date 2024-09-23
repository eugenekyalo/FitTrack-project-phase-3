import subprocess
import os

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def run_fittrack_command(command, *args):
    full_command = ["./fittrack.sh", command] + list(args)
    result = subprocess.run(full_command, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("Error:", result.stderr)
    input("Press Enter to continue...")

def create_user():
    name = input("Enter user name: ")
    age = input("Enter user age: ")
    height = input("Enter user height (in cm): ")
    weight = input("Enter user weight (in kg): ")
    fitness_level = input("Enter fitness level: ")
    run_fittrack_command("create_user", name, age, height, weight, fitness_level)

def log_workout():
    user_id = input("Enter user ID: ")
    exercise = input("Enter workout type: ")
    duration = input("Enter workout duration (in minutes): ")
    calories_burned = input("Enter calories burned: ")

    # Validate inputs
    if not user_id or not exercise or not duration or not calories_burned:
        print("All fields are required. Please provide valid inputs.")
        input("Press Enter to continue...")
        return

    # Ensure duration and calories are integers
    try:
        duration = int(duration)
        calories_burned = int(calories_burned)
    except ValueError:
        print("Duration and calories burned must be valid integers.")
        input("Press Enter to continue...")
        return

    # Print the arguments to be passed for debugging
    print("Logging workout with the following parameters:")
    print(f"User ID: {user_id}, Exercise: {exercise}, Duration: {duration}, Calories Burned: {calories_burned}")

    run_fittrack_command("log_workout", user_id, exercise, str(duration), str(calories_burned))

def log_nutrition():
    user_id = input("Enter user ID: ")
    food_item = input("Enter food item: ")
    calories = input("Enter calorie count: ")
    run_fittrack_command("log_nutrition", user_id, food_item, calories)

def journal_mental_health():
    user_id = input("Enter user ID: ")
    entry = input("Enter mental health journal entry: ")
    run_fittrack_command("journal_mental_health", user_id, entry)

def calculate_bmi():
    user_id = input("Enter user ID: ")
    run_fittrack_command("calculate_bmi", user_id)

def delete_user():
    user_id = input("Enter user ID to delete: ")
    run_fittrack_command("delete_user", user_id)

def main_menu():
    while True:
        clear_screen()
        print("Main Menu:")
        print("1. Create User")
        print("2. Log Workout")
        print("3. Log Nutrition")
        print("4. Journal Mental Health")
        print("5. Calculate BMI")
        print("6. Delete User")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_user()
        elif choice == '2':
            log_workout()
        elif choice == '3':
            log_nutrition()
        elif choice == '4':
            journal_mental_health()
        elif choice == '5':
            calculate_bmi()
        elif choice == '6':
            delete_user()
        elif choice == '7':
            print("Thank you for using FitTrack. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main_menu()
