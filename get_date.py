from datetime import datetime

def get_custom_date():
    today = datetime.today()
    month = today.month
    day = 22
    months = {
        1: "января",
        2: "февраля",
        3: "марта",
        4: "апреля",
        5: "мая",
        6: "июня",
        7: "июля",
        8: "августа",
        9: "сентября",
        10: "октября",
        11: "ноября",
        12: "декабря"
    }
    short_year = today.year % 100
    return f"на {day:02d} {months[month]} {short_year}"


