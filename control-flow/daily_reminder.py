task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is the time-bound? (yes/no): ").lower()

match priority:
    case "high":
        message = f"REMINDER: '{task}' needs is a high priority task that requires immediate attention today!."
    case "medium":
        message = f"REMINDER: '{task}' should be completed soon."
    case "low":
        message = f"REMINDER: '{task}' is a low priority task. Consider completing it when you have free time.."
    case _:
        message = f"REMINDER: The priority level for '{task}' is not recognized. Please check."

if time_bound == "yes":
    message += " This is a time-sensitive task"

print(message)