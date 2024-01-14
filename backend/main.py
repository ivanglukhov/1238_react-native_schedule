from flask import Flask
from flask_cors import CORS, cross_origin
import sqlite3




connection = sqlite3.connect("database.db", check_same_thread=False)
cursor = connection.cursor()

'''cursor.execute("DROP TABLE Schedule")'''

cursor.execute('''CREATE TABLE IF NOT EXISTS Schedule (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    day_of_week VARCHAR NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    subject VARCHAR NOT NULL,
    group_id VARCHAR(3) NOT NULL
); ''')

time = {
    1: ['8:00','8:40'],
    2: ['9:00','9:40'],
    3: ['10:00','10:40'],
    4: ['11:00','11:40'],
    5: ['12:00','12:40'],
    6: ['13:00','13:40'],
    7: ['14:00','14:40']
}


schedule = [['Русский язык',
  'Русский язык',
  'Литература',
  'Литература',
  'Литература',
  'Иностранный язык'],
 ['Иностранный язык',
  'Иностранный язык',
  'Математика(Алгебра)',
  'Математика(Алгебра)',
  'Математика(Алгебра)',
  'Математика(Алгебра)',
  'Физическая культура'],
 ['Математика(Геометрия)',
  'Математика(Геометрия)',
  'Математика(Геометрия)',
  'Математика(Тервер)',
  'Информатика',
  'Информатика',
  'ОБЖ'],
 ['Информатика', 'Информатика', 'Физика', 'Физика', 'Биология', 'Химия'],
 ['История',
  'История',
  'Обществознание',
  'Обществознание',
  'География',
  'Физическая культура']]


dw = ["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]

def writeSchedule():
    for day in range(len(schedule)):
        for i in range(len(schedule[day])):
            d = dw[day]
            s_t = time[i+1][0]
            e_t = time[i+1][1]
            s = schedule[day][i]
            g_r = '11А'
            
            print(f'''INSERT INTO Schedule (day_of_week, start_time, end_time, subject, group_id) 
            VALUES({d},{s_t},{e_t},{s},{g_r})''')
            cursor.execute(f'''INSERT INTO Schedule (day_of_week, start_time, end_time, subject, group_id) 
            VALUES("{d}","{s_t}","{e_t}","{s}","{g_r}")''')

            connection.commit()

writeSchedule()


def select_day_schedule(day, group):
    select = cursor.execute(f'''SELECT * FROM Schedule
    WHERE day_of_week="{day}" AND group_id ="{group}"''')
    select = cursor.fetchall()
    print(select)
    return select


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

@app.route("/<day_of_week>/<group>")
@cross_origin()
def get_day_schedule(day_of_week, group):
    day = day_query_translate[day_of_week]
    select=select_day_schedule(day, group)
    return select

