import React from "react";
import { styled } from "@mui/material/styles";
import Box from "@mui/material/Box";

const Slider = styled(Box, {
  shouldForwardProp: (prop) => prop !== "isActive",
})(({ isActive, theme }) => ({
  display: "inline-block",
  border: "2px solid #EF4B4B",
  padding: 8,
  borderRadius: "50%",
  cursor: "pointer",
  margin: "0 2px 0 2px",
  ...(isActive
    ? { backgroundColor: "#EF4B4B" }
    : {
        "&:hover": {
          backgroundColor: "#fac9c9",
          transition: "background-color 0.2s linear",
        },
      }),
}));
export default Slider;
