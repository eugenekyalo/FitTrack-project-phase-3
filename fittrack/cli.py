import argparse
from fittrack.models import Session, User, PhysicalGoal, Workout, NutritionLog, MentalHealthLog

def create_user(name, age, height, weight, fitness_level):
    session = Session()
    new_user = User(name=name, age=age, height=height, weight=weight, fitness_level=fitness_level)
    session.add(new_user)
    session.commit()
    print(f'User "{name}" created successfully.')
    session.close()

def set_physical_goal(user_id, goal):
    session = Session()
    physical_goal = PhysicalGoal(user_id=user_id, goal=goal)
    session.add(physical_goal)
    session.commit()
    print(f'Physical goal set for user ID {user_id}: {goal}')
    session.close()

def log_workout(user_id, exercise, duration, calories_burned):
    session = Session()
    workout = Workout(user_id=user_id, exercise=exercise, duration=duration, calories_burned=calories_burned)
    session.add(workout)
    session.commit()
    print(f'Logged workout for user ID {user_id}: {exercise}, {duration} mins, {calories_burned} calories burned.')
    session.close()

def log_nutrition(user_id, meal, calories):
    session = Session()
    nutrition_log = NutritionLog(user_id=user_id, meal=meal, calories=calories)
    session.add(nutrition_log)
    session.commit()
    print(f'Logged nutrition for user ID {user_id}: {meal}, {calories} calories.')
    session.close()

def journal_mental_health(user_id, entry):
    session = Session()
    mental_health_log = MentalHealthLog(user_id=user_id, entry=entry)
    session.add(mental_health_log)
    session.commit()
    print(f'Logged mental health entry for user ID {user_id}: {entry}')
    session.close()

def calculate_bmi(user_id):
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        height_m = user.height / 100  # convert height from cm to meters
        bmi = user.weight / (height_m ** 2)
        print(f'User ID {user_id} BMI: {bmi:.2f}')
    else:
        print(f'User ID {user_id} not found.')
    session.close()

def delete_user(user_id):
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print(f'User ID: {user_id} deleted successfully.')
    else:
        print(f'User ID: {user_id} not found.')
    session.close()

def main():
    parser = argparse.ArgumentParser(description='FitTrack CLI')
    subparsers = parser.add_subparsers(dest='command')

    # Create user
    create_user_parser = subparsers.add_parser('create-user')
    create_user_parser.add_argument('--name', required=True)
    create_user_parser.add_argument('--age', type=int, required=True)
    create_user_parser.add_argument('--height', type=float, required=True)
    create_user_parser.add_argument('--weight', type=float, required=True)
    create_user_parser.add_argument('--fitness-level', required=True)

    # Set physical goal
    set_goal_parser = subparsers.add_parser('set-physical-goal')
    set_goal_parser.add_argument('--user-id', type=int, required=True)
    set_goal_parser.add_argument('--goal', required=True)

    # Log workout
    log_workout_parser = subparsers.add_parser('log-workout')
    log_workout_parser.add_argument('--user-id', type=int, required=True)
    log_workout_parser.add_argument('--exercise', required=True)
    log_workout_parser.add_argument('--duration', type=int, required=True)
    log_workout_parser.add_argument('--calories-burned', type=int, required=True)

    # Log nutrition
    log_nutrition_parser = subparsers.add_parser('log-nutrition')
    log_nutrition_parser.add_argument('--user-id', type=int, required=True)
    log_nutrition_parser.add_argument('--meal', required=True)
    log_nutrition_parser.add_argument('--calories', type=int, required=True)

    # Journal mental health
    journal_parser = subparsers.add_parser('journal-mental-health')
    journal_parser.add_argument('--user-id', type=int, required=True)
    journal_parser.add_argument('--entry', required=True)

    # Calculate BMI
    calculate_bmi_parser = subparsers.add_parser('calculate-bmi')
    calculate_bmi_parser.add_argument('--user-id', type=int, required=True)

    # Delete user
    delete_user_parser = subparsers.add_parser('delete-user')
    delete_user_parser.add_argument('--user-id', type=int, required=True)

    args = parser.parse_args()

    if args.command == 'create-user':
        create_user(args.name, args.age, args.height, args.weight, args.fitness_level)
    elif args.command == 'set-physical-goal':
        set_physical_goal(args.user_id, args.goal)
    elif args.command == 'log-workout':
        log_workout(args.user_id, args.exercise, args.duration, args.calories_burned)
    elif args.command == 'log-nutrition':
        log_nutrition(args.user_id, args.meal, args.calories)
    elif args.command == 'journal-mental-health':
        journal_mental_health(args.user_id, args.entry)
    elif args.command == 'calculate-bmi':
        calculate_bmi(args.user_id)
    elif args.command == 'delete-user':
        delete_user(args.user_id)

if __name__ == '__main__':
    main()
