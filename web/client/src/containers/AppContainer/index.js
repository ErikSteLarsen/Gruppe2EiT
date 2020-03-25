import React from 'react';
import './styles.css';

import WeightMonitorContainer from '../WeightMonitorContainer';

import AppHeader from '../../components/AppHeader';

const AppContainer = () => {
  
  return (
    <div className="AppContainer">
      <AppHeader />
      <WeightMonitorContainer />
    </div>
  );
}

export default AppContainer;
