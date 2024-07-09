from datetime import datetime, timedelta
#from goit_pycore_hw_03_01 import get_days_from_today

def get_days_from_today(date):
    today = datetime.today().date()
    return (today - date).days

def get_upcoming_birthdays(users):
    users_to_congratulate = []
    for user in users:
        users_next_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        users_next_birthday = datetime(year = datetime.today().year, month = users_next_birthday.month, day = users_next_birthday.day).date()
        if users_next_birthday < datetime.today().date():
            users_next_birthday = datetime(year = datetime.today().year + 1, month = users_next_birthday.month, day = users_next_birthday.day).date()
        users_next_birthday_in = get_days_from_today(users_next_birthday)
        if users_next_birthday_in > 0 or users_next_birthday_in <= -7:
            continue
        else:
            congratulation_day = users_next_birthday
            if users_next_birthday.weekday() == 5:
                congratulation_day += timedelta(days = 2)
            elif users_next_birthday.weekday() == 6:
                congratulation_day += timedelta(days = 1)
            user_dict = {}
            user_dict["name"] = user["name"]
            user_dict["congratulation_date"] = datetime.strftime(congratulation_day, "%Y.%m.%d")
            users_to_congratulate.append(user_dict)
    return users_to_congratulate

users = [
    {"name": "John Doe", "birthday": "1985.07.08"},
    {"name": "Jane Smith", "birthday": "1990.07.09"},
    {"name": "Sam Reich", "birthday": "1990.07.10"},
    {"name": "Brennan Lee Mulligan", "birthday": "1990.07.13"},
    {"name": "Rekha Shankar", "birthday": "1990.07.14"},
    {"name": "Grant O'Brian", "birthday": "1990.07.16"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("People to congratulate this week:", upcoming_birthdays)
