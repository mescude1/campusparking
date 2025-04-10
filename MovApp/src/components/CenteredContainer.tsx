import React from 'react';
import { View, StyleSheet, ViewStyle } from 'react-native';

interface CenteredContainerProps {
  children?: React.ReactNode;
  style?: ViewStyle;
  marginTop?: number; // Allow custom top margin
  padding?: number; // Allow custom padding inside the container
}

const CenteredContainer: React.FC<CenteredContainerProps> = ({
  children,
  style,
  marginTop = 15,
  padding = 10, // Default padding inside the container
}) => {
  return (
    <View style={styles.wrapper}>
      <View style={[styles.container, { marginTop, padding }, style]}>{children}</View>
    </View>
  );
};

const styles = StyleSheet.create({
  wrapper: {
    flex: 1,
    alignItems: 'center', // Centers the container horizontally
  },
  container: {
    width: 380, // Adjust as needed
    height: 300, // Adjust as needed
    backgroundColor: 'white',
    borderRadius: 15,
    alignItems: 'flex-start', // Aligns contents to the left
    justifyContent: 'flex-start', // Aligns contents to the top
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 4,
    elevation: 5, // Android shadow
    marginTop: 10
  },
});

export default CenteredContainer;
