import React, { useState, useEffect } from "react";
import { Box, Typography } from "@mui/material";
import CustomerReview from "../CustomerReview/CustomerReview";
import Sliders from "../Sliders/Sliders";
import useStyles from "./style";
const customers = [
  {
    id: 1,
    pictureUrl: "/images/profiles_pictures/kevin_dockx.jpeg",
    name: "Kevin Dockx",
    comment:
      "This Pomotivity works considerably well. It recklessly improves my productivity by a lot.",
  },
  {
    id: 2,
    pictureUrl: "/images/profiles_pictures/brad_traversy.jpeg",
    name: "Brad Traversy",
    comment:
      "My neighbor Victoria use it. She works as a professor and she says it works phenomenal.",
  },
  {
    id: 3,
    pictureUrl: "/images/profiles_pictures/maximilian_schwarzmüller.jpeg",
    name: "Maximilian Schwarzmüller",
    comment:
      "Thanks guys, keep up the good work! I would be lost without Pomotivity. I couldn't have asked for more than this. I am really satisfied with my Pomotivity.",
  },
  {
    id: 4,
    pictureUrl: "/images/profiles_pictures/joshua_fluke.jpg",
    name: "Joshua Fluke",
    comment:
      "You guys rock! Thank you for making it painless, pleasant and most of all hassle free! Absolutely wonderful!",
  },
  {
    id: 5,
    pictureUrl: "/images/profiles_pictures/clement_mihailescu.jpeg",
    name: "Clement Mihailescu",
    comment:
      "Keep up the excellent work. Needless to say we are extremely satisfied with the results. Pomotivity is the most valuable business resource we have EVER purchased. I use Pomotivity often.",
  },
];
export default function CustomerReviewSlider() {
  const classes = useStyles();
  const [index, setIndex] = useState(0);
  const switchCustomerHandle = (index) => {
    setIndex(index);
  };
  useEffect(() => {
    const id = setTimeout(
      () => setIndex(index !== customers.length - 1 ? index + 1 : 0),
      5000
    );
    return () => {
      clearInterval(id);
    };
  });
  return (
    <Box className={classes.box}>
      <Typography
        variant="h5"
        color="initial"
        mb={2}
        sx={{ fontFamily: "'Days One', sans-serif;" }}
      >
        What our users say
      </Typography>
      <CustomerReview {...customers[index]} />
      <Box sx={{ margin: "8px 0px" }}></Box>
      <Sliders
        nSliders={customers.length}
        currentActive={index}
        switchCustomerFunction={switchCustomerHandle}
      />
    </Box>
  );
}
