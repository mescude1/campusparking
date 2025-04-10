import React, {useCallback, useState} from 'react';

import {useData, useTheme, useTranslation} from '../hooks/';
import {Block, Button, Image, Input, Product, Text} from '../components/';
import GreetUser from '../components/GreetUser'
import CenteredContainer from '../components/CenteredContainer'
import { View } from 'react-native';
const Home = () => {
  const {t} = useTranslation();
  const [tab, setTab] = useState<number>(0);
  const {valet_user, valet_driver} = useData();
  const [products, setProducts] = useState(valet_user);
  const {assets, colors, fonts, gradients, sizes} = useTheme();

  return (
      <CenteredContainer
                scroll
                horizontal
                renderToHardwareTextureAndroid
                showsHorizontalScrollIndicator={false}
                contentOffset={{x: -sizes.padding, y: 0}}>
        <GreetUser useSafeArea={true} />
      </CenteredContainer>
  );
};

export default Home;
