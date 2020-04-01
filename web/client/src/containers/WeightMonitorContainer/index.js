import React, { useState, useEffect } from 'react';
import './styles.css'
import { } from '@material-ui/core';
import RegistrationPlate from '../RegistrationPlate';
import FeedbackContainer from '../FeedbackContainer';

const WeightMonitorContainer = () => {
  const [hasError, setErrors] = useState(false);
  const [latestResult, setLatestResult] = useState({});

  const fetchData = async () => {
    const res = await fetch("/api/results/latest");
    res
      .json()
      .then(res => setLatestResult(res))
      .catch(err => setErrors(err));
  }

  useEffect(() => {
    fetchData();
  }, []);

  if (hasError) return (<div className="errorContainer">Something went wrong</div>)

  return (
    <div className="WeightMonitorContainer">
      <RegistrationPlate truck={latestResult.truck_details} />
      <FeedbackContainer testResults={latestResult.requirement_tests} />

      {latestResult && (<span>Raw: {JSON.stringify(latestResult)}</span>) }
    </div>
  )
}

export default WeightMonitorContainer;
