import React from 'react';
import './styles.css';
import { Grid, Paper} from '@material-ui/core';

const FeedbackContainer = () => {
  const truckPlate = "KJ29203"
  const trailerPlate = "KS1860"
  return (
    <div className="FeedbackContainer">
      <Grid spacing={3}
        container
        direction="column"
        justify="space-around"
        alignItems="stretch"
        style={{maxHeight:"60vh"}}>

        <Grid item xs>
          <Paper style={{backgroundColor: "red"}}>TEST RESULTAT</Paper>
        </Grid>
        <Grid item xs>
          <Paper style={{backgroundColor: "red"}}>TEST RESULTAT</Paper>
        </Grid>
        <Grid item xs>
          <Paper style={{backgroundColor: "green"}}>TEST RESULTAT</Paper>
        </Grid>
        <Grid item xs>
          <Paper style={{backgroundColor: "red"}}>TEST RESULTAT</Paper>
        </Grid>
        <Grid item xs>
          <Paper style={{backgroundColor: "green"}}>TEST RESULTAT</Paper>
        </Grid>
        <Grid item xs>
          <Paper style={{backgroundColor: "red"}}>TEST RESULTAT</Paper>
        </Grid>
        <Grid item xs>
          <Paper style={{backgroundColor: "red"}}>TEST RESULTAT</Paper>
        </Grid>
        <Grid item xs>
          <Paper style={{backgroundColor: "green"}}>TEST RESULTAT</Paper>
        </Grid>
        <Grid item xs>
          <Paper style={{backgroundColor: "red"}}>TEST RESULTAT</Paper>
        </Grid>
        <Grid item xs>
          <Paper style={{backgroundColor: "green"}}>TEST RESULTAT</Paper>
        </Grid>

      </Grid>
    </div>
  );
}

export default FeedbackContainer;
