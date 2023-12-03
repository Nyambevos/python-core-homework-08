from datetime import date, datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    DATE_NOW = date.today()

    in_users = users
    users = defaultdict(list)
    target_days = defaultdict(list)

    if len(in_users) == 0:
        return {}

    for i in range(0, 7):
        target_date = DATE_NOW + timedelta(i)
        target_days[target_date.month].append(target_date.day)

    for user in in_users:
        data_birthday = None

        if user["birthday"] >= DATE_NOW:
            data_birthday = user["birthday"]
        else:
            data_birthday = user["birthday"].replace(year=DATE_NOW.year + 1)

        if data_birthday.weekday() in [5, 6]:
            data_birthday += timedelta(7 - data_birthday.weekday())

        if data_birthday.month in target_days:
            if data_birthday.day in target_days[data_birthday.month]:
                users[data_birthday.strftime("%A")].append(user["name"])

    return dict(users)


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
