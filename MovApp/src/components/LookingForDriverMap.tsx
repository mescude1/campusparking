// components/LookingForDriverMap.tsx

import React, { useEffect, useRef, useState } from 'react';
import { View, Text, StyleSheet, Animated, Image, Dimensions } from 'react-native';
import MapView, { Marker, PROVIDER_GOOGLE, Region } from 'react-native-maps';
import * as Location from 'expo-location';

const { width } = Dimensions.get('window');

const mockDrivers = [
  { id: 1, latitudeDelta: 0.002, longitudeDelta: 0.002 },
  { id: 2, latitudeDelta: -0.0015, longitudeDelta: 0.0015 },
  { id: 3, latitudeDelta: 0.001, longitudeDelta: -0.001 },
];

export default function LookingForDriverMap() {
  const [region, setRegion] = useState<Region | null>(null);
  const swingAnim = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    (async () => {
      let { status } = await Location.requestForegroundPermissionsAsync();
      if (status !== 'granted') return;

      let location = await Location.getCurrentPositionAsync({});
      setRegion({
        latitude: location.coords.latitude,
        longitude: location.coords.longitude,
        latitudeDelta: 0.01,
        longitudeDelta: 0.01,
      });
    })();
  }, []);

  useEffect(() => {
    Animated.loop(
      Animated.sequence([
        Animated.timing(swingAnim, {
          toValue: 1,
          duration: 500,
          useNativeDriver: true,
        }),
        Animated.timing(swingAnim, {
          toValue: -1,
          duration: 500,
          useNativeDriver: true,
        }),
      ])
    ).start();
  }, []);

  const rotate = swingAnim.interpolate({
    inputRange: [-1, 1],
    outputRange: ['-15deg', '15deg'],
  });

  return (
    <View style={styles.container}>
      {region && (
        <MapView
          provider={PROVIDER_GOOGLE}
          style={StyleSheet.absoluteFillObject}
          region={region}
          showsUserLocation
        >
          {mockDrivers.map((driver, index) => (
            <Marker
              key={driver.id}
              coordinate={{
                latitude: region.latitude + driver.latitudeDelta,
                longitude: region.longitude + driver.longitudeDelta,
              }}
              title={`Driver ${index + 1}`}
              description="Nearby driver"
            />
          ))}
        </MapView>
      )}

      <View style={styles.overlayCard}>
        <Text style={styles.cardText}>Looking for driver...</Text>
        <Animated.Image
          source={require('../assets/keys.png')} // Place a keys.png file in assets
          style={[styles.keysIcon, { transform: [{ rotate }] }]}
        />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1 },
  overlayCard: {
    position: 'absolute',
    top: 60,
    alignSelf: 'center',
    backgroundColor: 'white',
    padding: 20,
    borderRadius: 16,
    flexDirection: 'row',
    alignItems: 'center',
    elevation: 4,
    shadowColor: '#000',
    shadowOpacity: 0.3,
    shadowRadius: 10,
    shadowOffset: { width: 0, height: 3 },
  },
  cardText: {
    fontSize: 18,
    fontWeight: '600',
    marginRight: 10,
  },
  keysIcon: {
    width: 40,
    height: 40,
  },
});
