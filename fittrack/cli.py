import argparse
from fittrack.models import session, User

def create_user(name, age, height, weight, fitness_level):
    user = User(name=name, age=age, height=height, weight=weight, fitness_level=fitness_level)
    session.add(user)
    session.commit()
    return f"User '{name}' created successfully."

def main():
    parser = argparse.ArgumentParser(description='FitTrack CLI')
    parser.add_argument('--create-user', action='store_true', help='Create a new user')
    parser.add_argument('--name', type=str, help='Name of the user')
    parser.add_argument('--age', type=int, help='Age of the user')
    parser.add_argument('--height', type=int, help='Height of the user')
    parser.add_argument('--weight', type=int, help='Weight of the user')
    parser.add_argument('--fitness-level', type=str, help='Fitness level of the user')
    
    args = parser.parse_args()
    
    if args.create_user:
        if args.name and args.age and args.height and args.weight and args.fitness_level:
            message = create_user(args.name, args.age, args.height, args.weight, args.fitness_level)
            print(message)
        else:
            print("Missing arguments for creating user")

if __name__ == '__main__':
    main()
