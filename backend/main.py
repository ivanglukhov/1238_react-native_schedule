from flask import Flask
from flask_cors import CORS, cross_origin
import sqlite3
from datetime import date, timedelta

def create_week_dict():
    dw = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]
    date_list = []
    today = date.today()
    start = today - timedelta(days=today.weekday()+1)
    for day in range(0,7):
        next = start + timedelta(days=day)
        date_list.append([str(next), dw[next.weekday()]])

    return date_list

connection = sqlite3.connect("schedule.db", check_same_thread=False)
cursor = connection.cursor()

time = {
    1: ['8:00','8:40'],
    2: ['9:00','9:40'],
    3: ['10:00','10:40'],
    4: ['11:00','11:40'],
    5: ['12:00','12:40'],
    6: ['13:00','13:40'],
    7: ['14:00','14:40']
}



dw = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]



def select_day_schedule(group):
    select = cursor.execute(f'''SELECT * FROM schedule
    WHERE group_id ="{group}"''')
    select = cursor.fetchall()
    week_list = create_week_dict()

    temp_d = {}
    for i in select:
        if i[1] not in temp_d:
            temp_d[i[1]] = []
        else:
            temp_d[i[1]].append(i[4])
    temp_d['Суббота'] = []
    temp_d['Воскресенье'] = []

    res_d = []

    for i in week_list:
        r_d = {}
        r_d['date'] = i[0]
        r_d['week_day'] = i[1]
        r_d['lessons'] = temp_d[i[1]]
        res_d.append(r_d)


    return res_d


day_query_translate = {
    'monday':"Понедельник",
    'tuesday': "Вторник",
    'wednesday': "Среда",
    'thursday': "Четверг",
    'friday': "Пятница",
    'saturday': "Суббота",
    'sunday': "Воскресенье",

}


app = Flask(__name__)
cors = CORS(app)

@app.route("/<group>")
@cross_origin()
def get_day_schedule(group):
    select=select_day_schedule(group)
    return select

app.run(debug=True)

