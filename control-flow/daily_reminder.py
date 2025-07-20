# daily_reminder.py

# 1. Gather inputs
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# 2. Provide a customized reminder directly in each branch
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        if time_bound == "yes":
            print(f"Reminder: '{task}' has an unspecified priority but requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' has an unspecified priority.")

# 3. Final congratulatory prompt
print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
print("🚀 Click here to tweet! 🚀")
