from datetime import date, datetime


def get_birthdays_per_week(users):
    in_users = users
    users = {}
    if len(in_users) == 0:
        return {}
    
    for user in in_users:
        if user["birthday"] < datetime.now().date():
            continue

    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
