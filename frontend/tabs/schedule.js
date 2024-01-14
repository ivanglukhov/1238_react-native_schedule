import { StyleSheet, Text, View, TouchableOpacity, StatusBar } from 'react-native';
import { Agenda, LocaleConfig } from 'react-native-calendars'


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



export default function Schedule() {

    let today = new Date();
    let dd = String(today.getDate()).padStart(2,'0');
    let mm = String(today.getMonth() + 1).padStart(2,'0');
    let yyyy = today.getFullYear()
    today = yyyy + '.' + mm + '.' + dd


    return (
        <View styles={styles.container}>
            <Agenda styles={styles.schedule}
                selected={today}
                items={{
                    '2023-12-19': [{name: 'Математика'}, {name: 'Физика'}, {name: 'Физика'}]
                }}
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