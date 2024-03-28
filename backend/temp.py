from datetime import date, timedelta

def create_week_dict():
    dw = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]
    date_list = []
    today = date.today()
    start = today - timedelta(days=today.weekday()+1)
    for day in range(0,7):
        next = start + timedelta(days=day)
        date_list.append({str(next): dw[next.weekday()]})

    return date_list