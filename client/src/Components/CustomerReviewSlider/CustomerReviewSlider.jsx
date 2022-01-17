import React, { useState, useEffect } from "react";
import { Box, Typography } from "@mui/material";
import CustomerReview from "../CustomerReview/CustomerReview";
import Sliders from "../Sliders/Sliders";
import useStyles from "./style";
const customers = [
  {
    id: 1,
    pictureUrl: "https://mvp.microsoft.com/zh-tw/PublicProfile/Photo/5000531",
    name: "Kevin Dockx",
    comment:
      "This Pomotivity works considerably well. It recklessly improves my productivity by a lot.",
  },
  {
    id: 2,
    pictureUrl:
      "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Favatars1.githubusercontent.com%2Fu%2F5550850%3Fs%3D400%26u%3Dfd608e37006781e0847825dc4045469eb4efbeed%26v%3D4&f=1&nofb=1",
    name: "Brad Traversy",
    comment:
      "My neighbor Victoria use it. She works as a professor and she says it works phenomenal.",
  },
  {
    id: 3,
    pictureUrl: "https://www.filepicker.io/api/file/TBHtUzkDTCykklB8apdG",
    name: "maximilian schwarzmüller",
    comment:
      "Thanks guys, keep up the good work! I would be lost without Pomotivity. I couldn't have asked for more than this. I am really satisfied with my Pomotivity.",
  },
  {
    id: 4,
    pictureUrl:
      "https://yt3.ggpht.com/a-/AAuE7mAG2AqrY2_yCmgb-rxFK1Dy_KUm918CwR99ag=s900-mo-c-c0xffffffff-rj-k-no",
    name: "Joshua Fluke",
    comment:
      "You guys rock! Thank you for making it painless, pleasant and most of all hassle free! Absolutely wonderful!",
  },
  {
    id: 5,
    pictureUrl:
      "https://qph.fs.quoracdn.net/main-qimg-fea66bd0eba283cc80151936b97fbee0",
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
