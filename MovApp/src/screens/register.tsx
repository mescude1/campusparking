// screens/Register.tsx
import React, { useState } from 'react';
import { Platform } from 'react-native';
import { useNavigation } from '@react-navigation/core';
import { Block, Button, Input, Image, Text } from '../components/';
import { useTheme } from '../hooks/';

const isAndroid = Platform.OS === 'android';

const Register = () => {
  const navigation = useNavigation();
  const { colors, assets, sizes } = useTheme();
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleRegister = () => {
    console.log('Register', { name, email, password });
  };

  const handleMicrosoftRegister = () => {
    console.log('Register with Microsoft');
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
              Registro
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
                placeholder="Nombre completo"
                marginBottom={sizes.m}
                value={name}
                onChangeText={(text) => setName(text)}
              />
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
              <Button onPress={handleRegister} color="#1E88E5" marginBottom={sizes.m}>
                <Text white bold center>Registrarme</Text>
              </Button>

              <Text center>o</Text>

              {/* Botón Microsoft */}
              <Button outlined color="#1E88E5" onPress={handleMicrosoftRegister} marginTop={sizes.m}>
                <Text bold color="#1E88E5">Registrarse con Microsoft</Text>
              </Button>

              <Button
                onPress={() => navigation.navigate('Login')}
                marginTop={sizes.m}
              >
                <Text center color="primary">¿Ya tienes cuenta? Inicia sesión</Text>
              </Button>
            </Block>
          </Block>
        </Block>
      </Block>
    </Block>
  );
};

export default Register;
