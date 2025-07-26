task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        message = f"REMINDER: '{task}' is a high priority task"
    case "medium":
        message = f"REMINDER: '{task}' should be completed soon."
    case "low":
        message = f"NOTE: '{task}' is a low priority task. Consider completing it when you have free time.."
    case _:
        message = f" '{task}' is not recognized. Please check."

if time_bound == "yes":
    message += "  that requires immediate attention today!"

print(message)
