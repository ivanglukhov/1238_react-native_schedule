import { StyleSheet, Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Schedule from './tabs/schedule.js'
import { MaterialCommunityIcons } from 'react-native-vector-icons';


export default function App() {

  const Tab = createBottomTabNavigator();

  return (
    <NavigationContainer>
      <Tab.Navigator>
        <Tab.Screen name="Расписание" component={Schedule} options={{
          tabBarIcon: () => (<MaterialCommunityIcons name="notebook-edit" size="40"/>) }}>
        </Tab.Screen>

      </Tab.Navigator>
    </NavigationContainer>
    
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
