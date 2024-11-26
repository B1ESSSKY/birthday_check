from datetime import date


def calculate_birthday_countdown(birthday):
    """
    Возвращает количество дней до следующего дня рождения.

    Если день рождения сегодня - возвращает 0.
    """
    today = date.today()
    this_year_birthday = get_birthday_for_year(birthday, today.year)

    if this_year_birthday < today:
        next_birthday = get_birthday_for_year(birthday, today.year + 1)
    else:
        next_birthday = this_year_birthday

    birthday_countdown = (next_birthday - today).days
    return birthday_countdown


def get_birthday_for_year(birthday, year):
    """
    Возвращает дату дня рождения в году.
    """
    try:
        calculated_birthday = birthday.replace(year=year)
    except ValueError:
        # День рождения выходит за рамки года
        calculated_birthday = date(year=year, month=3, day=1)

    return calculated_birthday
