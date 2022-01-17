import React from "react";
import TextField from "@mui/material/TextField";
import FormControl from "@mui/material/FormControl";
import InputLabel from "@mui/material/InputLabel";
import OutlinedInput from "@mui/material/OutlinedInput";
import InputAdornment from "@mui/material/InputAdornment";
import IconButton from "@mui/material/IconButton";
import Visibility from "@mui/icons-material/Visibility";
import VisibilityOff from "@mui/icons-material/VisibilityOff";
import FormGroup from "@mui/material/FormGroup";
import FormControlLabel from "@mui/material/FormControlLabel";
import Checkbox from "@mui/material/Checkbox";
import { Button, Typography } from "@mui/material";

export default function FormBody({
  username,
  usernameInputOnChange,
  password,
  passwordInputOnChange,
  showPassword,
  handleClickShowPassword,
  checked,
  handleClickOnCheckbox,
  handleSubmit,
}) {
  return (
    <form onSubmit={handleSubmit}>
      <TextField
        id="usernameInput"
        label="Username"
        variant="outlined"
        fullWidth
        margin="normal"
        value={username}
        onChange={usernameInputOnChange}
      />
      <FormControl variant="outlined" fullWidth margin="normal">
        <InputLabel htmlFor="outlined-adornment-password">Password</InputLabel>
        <OutlinedInput
          id="outlined-adornment-password"
          type={showPassword ? "text" : "password"}
          value={password}
          onChange={passwordInputOnChange}
          endAdornment={
            <InputAdornment position="end">
              <IconButton
                aria-label="toggle password visibility"
                onClick={handleClickShowPassword}
                edge="end"
              >
                {showPassword ? <VisibilityOff /> : <Visibility />}
              </IconButton>
            </InputAdornment>
          }
          label="Password"
        />
      </FormControl>
      <FormGroup>
        <FormControlLabel
          control={
            <Checkbox checked={checked} onClick={handleClickOnCheckbox} />
          }
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
      <Button
        variant="contained"
        color="primary"
        fullWidth
        sx={{ marginTop: 1 }}
        type="submit"
      >
        Sign up
      </Button>
    </form>
  );
}
