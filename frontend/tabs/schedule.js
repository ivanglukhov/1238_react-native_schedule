import { StyleSheet, Text, View, TouchableOpacity, StatusBar } from 'react-native';
import { Agenda, LocaleConfig } from 'react-native-calendars'
import { useState, useEffect } from 'react';


LocaleConfig.locales['ru'] = {
    monthNames: [
        'Январь',
        'Февраль',
        'Март',
        'Апрель',
        'Май',
        'Июнь',
        'Июль',
        'Август',
        'Сентябрь',
        'Октябрь',
        'Ноябрь',
        'Декабрь',
    ],
    monthNamesShort: [
        'Янв',
        'Фев',
        'Мар',
        'Апр',
        'Май',
        'Июн',
        'Июл',
        'Авг',
        'Сен',
        'Окт',
        'Ноя',
        'Дек',
    ],
    dayNames: [
        'воскресенье',
        'понедельник',
        'вторник',
        'среда',
        'четверг',
        'пятница',
        'суббота',
    ],
    dayNamesShort: ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'],
    today: 'Сегодня',
};
LocaleConfig.defaultLocale = 'ru';

function stringDate(today) { 
    let dd = String(today.getDate()).padStart(2,'0');
    let mm = String(today.getMonth() + 1).padStart(2,'0');
    let yyyy = today.getFullYear();
    let week = ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'];

    let day_of_week = week[today.getDay()]
    today = yyyy + '-' + mm + '-' + dd;

}

export default function Schedule() {

    let today = new Date();
    let dd = String(today.getDate()).padStart(2,'0');
    let mm = String(today.getMonth() + 1).padStart(2,'0');
    let yyyy = today.getFullYear();
    let week = ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'];

    let day_of_week = week[today.getDay()]
    today = yyyy + '-' + mm + '-' + dd;
   

    let fetch_url = 'http://127.0.0.1:5000/';
    var result_obj = {}

    const [schedule, setSchedule] = useState({});
    useEffect(() => {
            fetch("http://127.0.0.1:5000/11%D0%90").then((res) => {
                return res.json();
            }).then((json) => {
                let res = [];
                console.log(json);
                
                let result_obj = {}
                json.forEach(element => {
                        result_obj[element['date']] = [];
                        element['lessons'].forEach(lesson => {
                            result_obj[element['date']].push({'name': lesson});
                        });
                    }); 
                    setSchedule(result_obj); 
                }); 
    }, []);

    return (
        <View styles={styles.container}>
            <Agenda styles={styles.schedule}
                selected={today}
                items={schedule}
                renderItem={(item, isFirst) => (
                    <TouchableOpacity style={styles.item}>
                        <Text style={styles.itemText}>{item.name}</Text>
                    </TouchableOpacity>
                )}
            />
        </View>
    )
  }

  
const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#fff',
      alignItems: 'center',
      justifyContent: 'center',
    },
    schedule: {
        width: '100%'
    }
  });