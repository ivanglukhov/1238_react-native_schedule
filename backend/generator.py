import tkinter
import sqlite3

connection = sqlite3.connect('schedule.db')
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS schedule (
            id INTEGER PRIMARY KEY,
            day_of_week VARCHAR,
            start_time VARCHAR,
            end_time VARCHAR,
            subject VARCHAR,
            group_id VARCHAR(3)
)''')

d = {
    'Русский язык': [2, 9],
    'Литература': [3, 8],
    'Иностранный язык': [3, 8],
    'Математика(Алгебра)': [4, 10],
    'Математика(Геометрия)': [3, 11],
    'Математика(Тервер)': [1, 12],
    'Информатика': [4, 6],
    'Физика': [2, 12],
    'Биология': [1, 7],
    'Химия': [1, 11],
    'История': [2, 5],
    'Обществознание': [2, 5],
    'География': [1, 3],
    'Физическая культура': [2, 1],
    'ОБЖ': [1, 2]
}
bintb = []  # расписание в векторном виде
result_schedule = []

def swap(i, j, k):
    s = [1, 0]
    bintb[i][j][k] = s[bintb[i][j][k]]


def rating(schedule):
    lessons_names = list(d.keys())
    total_rating = 0
    lessons_count = [0 for i in range(0, 15)]
    used_error = 0
    difficult_error = 0
    for i in range(0, 5):  # день
        used_lessons = [0, 1, 2, 3, 4, 5, 6]
        diff_sum = 0
        count_by_day = 0
        for j in range(0, 15):  # предмет
            for k in range(0, 7):  # номер урока
                if bintb[i][j][k] == 1:
                    count_by_day += 1
                    diff_sum += d[lessons_names[j]][1]
                    lessons_count[j] += schedule[i][j][k]
        if diff_sum < 35 or diff_sum > 40 or count_by_day > 7:
            difficult_error += 1
    count_error = 0
    k = 0
    for i in d.keys():
        count_error += abs(d[i][0] - lessons_count[k])
        k += 1
    total_rating -= (count_error * 1000) + (difficult_error * 2000)
    return total_rating


def training(epochs):
    for e in range(epochs):
        cur_r = rating(bintb)
        for i in range(0, 5):  # день
            for j in range(0, 15):  # предмет
                for k in range(0, 7):  # номер урока
                    swap(i, j, k)
                    if (rating(bintb) < cur_r):
                        swap(i, j, k)


def create_schedule():
    for i in range(len(edits)):
        if edits[i][0].get() != '':
            e_subj = edits[i][0].get()
            e_hours = int(edits[i][1].get())
            e_diff = int(edits[i][2].get())
            d[e_subj] = [e_hours, e_diff]

    for i in range(0, 5):  # день
        day = []
        for j in range(0, 15):  # предмет
            lesson = []
            for k in range(0, 7):  # номер урока
                lesson.append(0)
            day.append(lesson)
        bintb.append(day)
    training(5000)

    lessons_names = list(d.keys())
    days = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ']
    all_less = 0
    global result_schedule
    for i in range(0, 5):
        l_c = 0

        res_day = []
        for j in range(0, 15):
            for k in range(0, 7):
                if bintb[i][j][k] == 1:
                    res_day.append(lessons_names[j])
                    l_c += 1
                    all_less += 1
                    print(l_c, 'урок', lessons_names[j])
                    result.insert(all_less, f"{l_c}, урок, {lessons_names[j]}")
        result_schedule.append(res_day)
    print(result_schedule)

def paste_bd():
    bd_days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
    bd_times_start = ['8:00','9:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00', '18:00','19:00','20:00']
    bd_times_end = ['8:40','9:40','10:40','11:40','12:40','13:40','14:40', '15:40', '16:40', '17:40', '18:40', '19:40', '20:40']
    group_id = '11А'

    for i in range(len(result_schedule)):
        for j in range(0, len(result_schedule[i])):
            print(bd_days[i], bd_times_start[j], bd_times_end[j], result_schedule[i][j], group_id)
            cursor.execute('INSERT INTO schedule(day_of_week, start_time, end_time, subject, group_id) VALUES (?,?,?,?,?)',
                           (bd_days[i], bd_times_start[j], bd_times_end[j], result_schedule[i][j], group_id))

            connection.commit()




window = tkinter.Tk()

inputs = tkinter.Frame(window)
subj = {}

tkinter.Label(inputs, text='Предмет').grid(row=1, column=1)
tkinter.Label(inputs, text='Кол-во часов').grid(row=1, column=2)
tkinter.Label(inputs, text='Сложность').grid(row=1, column=3)

edits = []
for i in range(2, 17):
    edit = []
    for j in range(1, 4):
        edit.append(tkinter.Entry(inputs))
        edit[j - 1].grid(row=i, column=j, padx=8, pady=1)

    sub = list(d.keys())[i - 2]
    edit[0].insert(0, sub)
    edit[1].insert(0, d[sub][0])
    edit[2].insert(0, d[sub][1])
    edits.append(edit)

tkinter.Label(inputs, text='Результат').grid(row=1, column=4)
result = tkinter.Listbox(inputs, )
result.grid(row=2, column=4, padx=8, pady=1)

paste_bd_button = tkinter.Button(inputs, text='Записать в базу данных', command=paste_bd)
paste_bd_button.grid(row=3, column=4, padx=8, pady=2)

inputs.pack()

confirm = tkinter.Button(text='Составить расписание', command=create_schedule)
confirm.pack()

window.mainloop()
