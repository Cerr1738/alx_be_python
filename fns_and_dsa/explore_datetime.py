

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Prompts the user for a number of days, calculates the future date,
    and displays it in the format YYYY-MM-DD.
    """
    try:
        days = int(input("Enter the number of days into the future: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
        formatted_future = future_date.strftime("%Y-%m-%d")
        print(f"The date after {days} days will be: {formatted_future}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

def main():
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
