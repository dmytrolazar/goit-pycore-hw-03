from datetime import datetime

def get_days_from_today(date):
    today = datetime.today().date()
    return (today - date).days

input = input("Enter a date in YYYY-MM-DD format: ")
try:
    inputdate = datetime.strptime(input, "%Y-%m-%d").date()
    datediff = get_days_from_today(inputdate)
    print(f"The difference between the date you entered and today's date is {datediff} day(s).")
except:
    print("Input string does not follow the correct format.")