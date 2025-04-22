import React from 'react';
import {createStackNavigator} from '@react-navigation/stack';

import {Articles, Components, Home, Profile, Login, Register, Pro} from '../screens';
import {useScreenOptions, useTranslation} from '../hooks';

const Stack = createStackNavigator();

export default () => {
  const {t} = useTranslation();
  const screenOptions = useScreenOptions();

  return (
    <Stack.Navigator screenOptions={screenOptions.stack}>
      <Stack.Screen
        name="Home"
        component={Home}
        options={{title: t('navigation.home')}}
      />
      <Stack.Screen
        name="Ultimos Servicios"
        component={Articles}
        options={{title: t('navigation.past_services_list')}}
      />
      <Stack.Screen
        name="Perfil"
        component={Profile}
        options={{headerShown: false, title: t('navigation.profile')}}
      />
      <Stack.Screen
        name="Register"
        component={Register}
        options={{headerShown: false, title: t('navigation.register')}}
      />
      <Stack.Screen
        name="Login"
        component={Login}
        options={{headerShown: false, title: t('navigation.login')}}
      />
    </Stack.Navigator>
  );
};
