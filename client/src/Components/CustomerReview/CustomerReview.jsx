import React from "react";
import Avatar from "@mui/material/Avatar";
import Typography from "@mui/material/Typography";
import { Box } from "@mui/system";

export default function CustomerReview({ profileUrl, name, comment }) {
  return (
    <Box
      sx={{ display: "flex", flexDirection: "column", alignItems: "center" }}
    >
      <Avatar
        alt={`${name} picture`}
        src={profileUrl}
        sx={{ width: 100, height: 100 }}
      />
      <Typography variant="h6" color="initial" sx={{ marginY: "4px" }}>
        {name}
      </Typography>
      <Typography variant="body1" color="initial" textAlign={"center"}>
        {comment}
      </Typography>
    </Box>
  );
}
