import subprocess

def setup_user(name, age, height, weight, fitness_level, goal, exercise, duration, calories):
    subprocess.run(["python", "fittrack/cli.py", "create-user", "--name", name, "--age", str(age), "--height", str(height), "--weight", str(weight), "--fitness-level", fitness_level])
    subprocess.run(["python", "fittrack/cli.py", "set-physical-goal", "--user-id", "2", "--goal", goal])
    subprocess.run(["python", "fittrack/cli.py", "log-workout", "--user-id", "2", "--exercise", exercise, "--duration", str(duration), "--calories-burned", str(calories)])

setup_user("Jane Doe", 28, 165, 60, "Beginner", "Run 5 km", "Jogging", 45, 400)
