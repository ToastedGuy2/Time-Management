import { Container, Grid } from "@mui/material";
import React from "react";
import CustomerReviewSlider from "../CustomerReviewSlider/CustomerReviewSlider";
import Form from "../Form/Form";
import useStyles from "./style";
import Box from "@mui/material/Box";
export default function SignUp() {
  const classes = useStyles();
  return (
    <Box className={classes.box}>
      <Container maxWidth="md" className={classes.container}>
        <Grid container spacing={2}>
          <Grid item md={6}>
            <CustomerReviewSlider />
          </Grid>
          <Grid item md={6}>
            <Form />
          </Grid>
        </Grid>
      </Container>
    </Box>
  );
}
