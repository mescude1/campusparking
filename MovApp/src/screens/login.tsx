// screens/Login.tsx
import React, { useState } from 'react';
import { Platform } from 'react-native';
import { useNavigation } from '@react-navigation/core';
import { Block, Button, Input, Image, Text } from '../components/';
import { useTheme } from '../hooks/';

const isAndroid = Platform.OS === 'android';

const Login = () => {
  const navigation = useNavigation();
  const { colors, assets, sizes } = useTheme();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    console.log('Login', { email, password });
  };

  const handleMicrosoftLogin = () => {
    console.log('Login with Microsoft');
  };

  return (
    <Block safe marginTop={sizes.md}>
      <Block paddingHorizontal={sizes.s}>
        {/* Header */}
        <Block flex={0} style={{ zIndex: 0 }}>
          <Image
            background
            resizeMode="cover"
            padding={sizes.sm}
            radius={sizes.cardRadius}
            source={assets.background}
            height={sizes.height * 0.3}
          >
            <Text h4 center white marginBottom={sizes.md}>
              Iniciar Sesión
            </Text>
          </Image>
        </Block>

        {/* Formulario */}
        <Block
          keyboard
          behavior={!isAndroid ? 'padding' : 'height'}
          marginTop={-(sizes.height * 0.2 - sizes.l)}
        >
          <Block
            flex={0}
            radius={sizes.sm}
            marginHorizontal="8%"
            shadow={!isAndroid}
          >
            <Block
              blur
              flex={0}
              intensity={90}
              radius={sizes.sm}
              overflow="hidden"
              justify="center"
              paddingVertical={sizes.sm}
            >
              <Input
                placeholder="Correo Institucional"
                keyboardType="email-address"
                autoCapitalize="none"
                marginBottom={sizes.m}
                value={email}
                onChangeText={(text) => setEmail(text)}
              />
              <Input
                placeholder="Contraseña"
                secureTextEntry
                marginBottom={sizes.m}
                value={password}
                onChangeText={(text) => setPassword(text)}
              />
              <Button onPress={handleLogin} color="#1E88E5" marginBottom={sizes.m}>
                <Text white bold center>Entrar</Text>
              </Button>

              <Text center>o</Text>

              {/* Botón Microsoft */}
              <Button outlined color="#1E88E5" onPress={handleMicrosoftLogin} marginTop={sizes.m}>
                <Text bold color="#1E88E5">Continuar con Microsoft</Text>
              </Button>

              <Button
                onPress={() => navigation.navigate('Register')}
                marginTop={sizes.m}
              >
                <Text center color="primary">¿No tienes cuenta? Regístrate</Text>
              </Button>
            </Block>
          </Block>
        </Block>
      </Block>
    </Block>
  );
};

export default Login;
