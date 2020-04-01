import React from 'react';
import './styles.css';
import { Grid, Paper} from '@material-ui/core';

const RegistrationPlate = (props) => {
  const truckPlate = props.truck && props.truck.truck_regnr;
  const trailerPlate = props.truck && props.truck.trailer_regnr;
  return (
    <div className="RegistrationPlate">
    <Grid container spacing={4}>

     <Grid item xs={12}>
          <Paper style={{backgroundColor: "#404652", color: "white", marginLeft:"20%", marginRight:"20%"}}>Registreringsnummer</Paper>
        </Grid>

      <Grid item xs={12} sm={6}>
        <Paper style={{marginLeft: "20%", backgroundColor: "#404652", color: "white"}}>Lastebil: {truckPlate}</Paper>
      </Grid>
      <Grid item xs={12} sm={6}>
        <Paper style={{marginRight: "20%", backgroundColor: "#404652", color: "white"}}>Henger: {trailerPlate}</Paper>
      </Grid>
    </Grid>
    </div>
  );
}

export default RegistrationPlate;
