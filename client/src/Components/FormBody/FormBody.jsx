import React from "react";
import TextField from "@mui/material/TextField";
import FormControl from "@mui/material/FormControl";
import InputLabel from "@mui/material/InputLabel";
import FilledInput from "@mui/material/FilledInput";
import InputAdornment from "@mui/material/InputAdornment";
import IconButton from "@mui/material/IconButton";
import Visibility from "@mui/icons-material/Visibility";
import VisibilityOff from "@mui/icons-material/VisibilityOff";
import FormGroup from "@mui/material/FormGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import { Button, Typography } from "@mui/material";

export default function FormBody({}) {
  return (
    <form>
      <TextField
        id="usernameInput"
        label="Username"
        variant="filled"
        fullWidth
        margin="normal"
      />
      <FormControl variant="outlined" fullWidth margin="normal">
        <InputLabel htmlFor="outlined-adornment-password">Password</InputLabel>
        <FilledInput
          id="outlined-adornment-password"
          type={true ? "text" : "password"}
          value=""
          onChange={() => {}}
          endAdornment={
            <InputAdornment position="end">
              <IconButton
                aria-label="toggle password visibility"
                onClick={() => {}}
                onMouseDown={() => {}}
                edge="end"
              >
                {true ? <VisibilityOff /> : <Visibility />}
              </IconButton>
            </InputAdornment>
          }
          label="Password"
        />
      </FormControl>
      {/* <FormGroup sx={{ m: "16px 0 16px 0px" }}> */}
      <FormGroup>
        <FormControlLabel
          control={<Checkbox defaultChecked />}
          //   label="By signing up, you agree to the"
          label={
            <Typography variant="span" color="initial">
              By signing up, you agree to the{" "}
              <Typography
                variant="span"
                color="primary"
                sx={{ fontWeight: 700 }}
              >
                Terms of Service
              </Typography>
            </Typography>
          }
        />
      </FormGroup>
      <Button variant="contained" color="primary" fullWidth>
        Sign up
      </Button>
    </form>
  );
}
{
  /* <FilledInput
          id="outlined-adornment-password"
          type={values.showPassword ? "text" : "password"}
          value={values.password}
          onChange={handleChange("password")}
          endAdornment={
            <InputAdornment position="end">
              <IconButton
                aria-label="toggle password visibility"
                onClick={handleClickShowPassword}
                onMouseDown={handleMouseDownPassword}
                edge="end"
              >
                {values.showPassword ? <VisibilityOff /> : <Visibility />}
              </IconButton>
            </InputAdornment>
          }
          label="Password"
        /> */
}
