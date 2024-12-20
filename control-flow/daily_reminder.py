# daily_reminder.py

# Prompt for task input
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process task based on priority and time sensitivity
match priority:
    case "high":
        message = f"'{task}' is a high priority task."
    case "medium":
        message = f"'{task}' is a medium priority task."
    case "low":
        message = f"'{task}' is a low priority task."
    case _:
        message = f"'{task}' has an unspecified priority. Please clarify."

# Add time sensitivity message
if time_bound == "yes":
    message += " It requires immediate attention today!"
else:
    message += " Consider completing it when you have free time."

# Print customized reminder
print("\nReminder:", message)

# Prompt to continue or exit
while True:
    proceed = input("\nDo you want to set another reminder? (yes/no): ").strip().lower()
    if proceed == "yes":
        exec(open(__file__).read())  # Restart script for a new task
        break
    elif proceed == "no":
        print("Goodbye!")

        break
    else:
        print("Invalid response. Please type 'yes' or 'no'.")