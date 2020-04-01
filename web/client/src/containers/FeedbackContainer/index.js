import React from 'react';
import './styles.css';
import { Grid, Paper} from '@material-ui/core';

const FeedbackContainer = (props) => {

  /*
   * Test Result
   *
   * Single Result <Grid> item
   *
   */
  const TestResult = (props) => {
    const { result } = props;
    return (
      <Grid item xs>
        <Paper style={result.pass ? {backgroundColor: "green"} : {backgroundColor: "red"}}>{result.test_name}</Paper>
      </Grid>
    )
  }


  /*
   * ResultList
   *
   * Array of <TestResult /> items with test name as key
   *
   */
  const ResultList = (props) => {
    const { results } = props;
    if (!results) return null;

    const testItems = results.map( testResult => (
      <TestResult key={testResult.test_name} result={testResult} />
    ));

    return testItems;
  }

  return (
    <div className="FeedbackContainer">
      <Grid spacing={3}
        container
        direction="column"
        justify="space-around"
        alignItems="stretch"
        style={{maxHeight:"60vh"}}>

        <ResultList results={props.testResults}/>
      </Grid>
    </div>
  );
}

export default FeedbackContainer;
