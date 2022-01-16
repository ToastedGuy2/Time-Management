import React from "react";
import { Link, Typography } from "@mui/material";

export default function FormFooter() {
  return (
    <Typography variant="body2" color="initial" align="center" mb={1} mt={2}>
      Already have an account?{" "}
      <Link variant="body2" color="primary" underline="hover" href="#">
        Sign in
      </Link>
    </Typography>
  );
}
