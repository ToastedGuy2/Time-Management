import { Box } from "@mui/material";
import React from "react";
import CustomerReview from "../CustomerReview/CustomerReview";
import Sliders from "../Sliders/Sliders";
import useStyles from "./style";
export default function CustomerReviewSlider() {
  const classes = useStyles();
  return (
    <Box className={classes.box} sx={{ display: { xs: "none", md: "flex" } }}>
      <CustomerReview
        profileUrl={
          "https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fnaibuzz.com%2Fwp-content%2Fuploads%2F2017%2F06%2FDave.jpeg&f=1&nofb=1"
        }
        name={"Dave2D"}
        comment={
          "Dolor dignissimos est amet vel repudiandae sunt nostrum. Dolores quia doloribus laboriosam repellat. Vel aut dolore sapiente est eius."
        }
      />
      <Box sx={{ margin: "8px 0px" }}></Box>
      <Sliders nSliders={3} currentActive={1} />
    </Box>
  );
}
