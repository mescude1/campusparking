import React, { useCallback, useState } from "react";

import { useData, useTheme, useTranslation } from "../hooks/";

import PaginatedTrips from "../components/PaginatedTrips";
import CenteredContainer from "../components/CenteredContainer";

const PastServicesList = () => {
  const { t } = useTranslation();
  const [tab, setTab] = useState<number>(0);
  const { valet_user, valet_driver } = useData();
  const [products, setProducts] = useState(valet_user);
  const { assets, colors, fonts, gradients, sizes } = useTheme();

  return (
    <CenteredContainer
      scroll
      horizontal
      renderToHardwareTextureAndroid
      showsHorizontalScrollIndicator={false}
      contentOffset={{ x: -sizes.padding, y: 0 }}
    >
      <PaginatedTrips />
    </CenteredContainer>
  );
};

export default PastServicesList;
