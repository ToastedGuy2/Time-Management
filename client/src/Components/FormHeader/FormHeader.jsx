import React from "react";
import Typography from "@mui/material/Typography";

export default function FormHeader({ title }) {
  return (
    <div>
      <Typography
        variant="h4"
        color="initial"
        align="center"
        sx={{ fontFamily: "'Days One', sans-serif;" }}
      >
        {title}
      </Typography>
      <Typography
        variant="h4"
        color="initial"
        align="center"
        sx={{ fontFamily: "'Days One', sans-serif;" }}
      >
        to
      </Typography>
      <div style={{ textAlign: "center" }}>
        <img
          src="/images/logo.png"
          alt=""
          srcSet=""
          style={{ height: "100px", width: "100px" }}
        />
      </div>
      <Typography
        variant="h3"
        color="primary"
        align="center"
        sx={{ fontFamily: "'Shrikhand', cursive;" }}
      >
        Pomotivity
      </Typography>
    </div>
  );
}
