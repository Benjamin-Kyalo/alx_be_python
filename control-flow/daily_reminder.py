# daily_reminder.py

# 1. Gather inputs
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# 2. Build the base message using match-case
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Note: '{task}' has an unspecified priority"

# 3. Modify based on time sensitivity
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if priority == "low":
        message += ". Consider completing it when you have free time."
    else:
        message += "."

# 4. Output the reminder
print("\n" + message)

# 5. Final congratulatory prompt
print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
print("🚀 Click here to tweet! 🚀")
