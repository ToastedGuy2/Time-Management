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
      <Container
        maxWidth="xs"
        className={classes.container}
        sx={{ display: { md: "none" } }}
      >
        <Form />
      </Container>
      <Container
        maxWidth="md"
        className={classes.container}
        sx={{ display: { xs: "none", md: "flex" } }}
      >
        <Grid container spacing={2} justifyContent={"center"}>
          <Grid item md={6} sx={{ display: "flex", alignItems: "center" }}>
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
