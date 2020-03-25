import React from 'react';
import './styles.css'
import { } from '@material-ui/core';
import RegistrationPlate from '../RegistrationPlate';
import FeedbackContainer from '../FeedbackContainer';

const WeightMonitorContainer = () => {
  return (
    <div className="WeightMonitorContainer">
        <RegistrationPlate />
        <FeedbackContainer />
    </div>
  )
}

export default WeightMonitorContainer;
