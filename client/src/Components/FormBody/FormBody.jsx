import React, { forwardRef } from "react";
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
import { theme } from "../../theme";
import {
  Alert,
  AlertTitle,
  Box,
  Button,
  CircularProgress,
  Collapse,
  Typography,
} from "@mui/material";
import {
  Dialog,
  DialogTitle,
  DialogContent,
  DialogContentText,
  DialogActions,
} from "@mui/material";
import FormHelperText from "@mui/material/FormHelperText";

import CheckIcon from "@mui/icons-material/Check";
const FormBody = forwardRef(
  (
    {
      username,
      usernameInputOnChange,
      password,
      passwordInputOnChange,
      showPassword,
      handleClickShowPassword,
      checked,
      handleClickOnCheckbox,
      handleSubmit,
      showModal,
      handleOpenModal,
      handleCloseModal,
      handleOnClickAcceptTerms,
      usernameError,
      passwordError,
      checkboxError,
      isRegisteringUser,
      showAlert,
      handleCloseAlert,
    },
    ref
  ) => {
    return (
      <div>
        <form onSubmit={handleSubmit}>
          <Collapse in={showAlert}>
            <Alert severity="error" variant="filled" onClose={handleCloseAlert}>
              <AlertTitle>Error</AlertTitle>
              OOPS something went wrong on our servers while processing your
              request. Please try again
            </Alert>
          </Collapse>
          <TextField
            id="usernameInput"
            label="Username"
            variant="outlined"
            fullWidth
            margin="normal"
            value={username}
            onChange={usernameInputOnChange}
            helperText={usernameError.error ? usernameError.errorMessage : ""}
            error={usernameError.error}
            disabled={isRegisteringUser}
          />
          <FormControl
            variant="outlined"
            fullWidth
            margin="normal"
            error={passwordError.error}
            disabled={isRegisteringUser}
          >
            <InputLabel htmlFor="outlined-adornment-password">
              Password
            </InputLabel>
            <OutlinedInput
              helperText={passwordError.error ? passwordError.errorMessage : ""}
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
            <FormHelperText>
              {passwordError.error
                ? passwordError.errorMessage
                : "MEMORIZE IT, since we have no account recovery method"}
            </FormHelperText>
          </FormControl>
          <FormControl error={checkboxError.error} disabled={isRegisteringUser}>
            <FormGroup>
              <FormControlLabel
                control={
                  <Checkbox
                    checked={checked}
                    onClick={handleClickOnCheckbox}
                    className={true && "Hello"}
                    sx={{
                      color: checkboxError.error
                        ? theme.palette.error.main
                        : "fff",
                    }}
                  />
                }
                label={
                  <>
                    By signing up, you agree to the{" "}
                    <Typography
                      variant="span"
                      color={isRegisteringUser ? "inherit" : "primary"}
                      sx={{ fontWeight: 700 }}
                      onClick={(event) => {
                        event.stopPropagation();
                        event.preventDefault();
                        handleOpenModal();
                      }}
                    >
                      Terms of Service
                    </Typography>
                  </>
                }
              />
              <FormHelperText>
                {checkboxError.error ? checkboxError.errorMessage : ""}
              </FormHelperText>
            </FormGroup>
          </FormControl>
          <Box sx={{ marginTop: 1, position: "relative" }}>
            <Button
              variant="contained"
              type="submit"
              disabled={isRegisteringUser}
              fullWidth
            >
              Sign up
            </Button>
            {isRegisteringUser && (
              <CircularProgress
                size={24}
                color="primary"
                sx={{
                  position: "absolute",
                  top: "50%",
                  left: "50%",
                  marginTop: "-12px",
                  marginLeft: "-12px",
                }}
              />
            )}
          </Box>
        </form>
        <Dialog
          open={showModal}
          onClose={handleCloseModal}
          aria-labelledby="scroll-dialog-title"
          aria-describedby="scroll-dialog-description"
        >
          <DialogTitle id="scroll-dialog-title">
            Website Terms and Conditions of Use
          </DialogTitle>
          <DialogContent dividers={true}>
            <DialogContentText
              id="scroll-dialog-description"
              ref={ref}
              tabIndex={-1}
            >
              <Typography variant="h6" gutterBottom component="div">
                1. Terms
              </Typography>
              <Typography variant="body1" gutterBottom component="div">
                By accessing this Website, accessible from Pomotivity.com, you
                are agreeing to be bound by these Website Terms and Conditions
                of Use and agree that you are responsible for the agreement with
                any applicable local laws. If you disagree with any of these
                terms, you are prohibited from accessing this site. The
                materials contained in this Website are protected by copyright
                and trade mark law.
              </Typography>
              <Typography variant="h6" gutterBottom component="div">
                2. Use License
              </Typography>
              <Typography variant="body1" gutterBottom component="div">
                Permission is granted to temporarily download one copy of the
                materials on Pomotivity Website for personal, non-commercial
                transitory viewing only. This is the grant of a license, not a
                transfer of title, and under this license you may not: modify or
                copy the materials; use the materials for any commercial purpose
                or for any public display; attempt to reverse engineer any
                software contained on Pomotivity Website; remove any copyright
                or other proprietary notations from the materials; or
                transferring the materials to another person or "mirror" the
                materials on any other server. This will let Company Name to
                terminate upon violations of any of these restrictions. Upon
                termination, your viewing right will also be terminated and you
                should destroy any downloaded materials in your possession
                whether it is printed or electronic format.
              </Typography>
              <Typography variant="h6" gutterBottom component="div">
                3. Disclaimer
              </Typography>
              <Typography variant="body1" gutterBottom component="div">
                All the materials on Pomotivity Website are provided “as is”.
                Company Name makes no warranties, may it be expressed or
                implied, therefore negates all other warranties. Furthermore,
                Company Name does not make any representations concerning the
                accuracy or reliability of the use of the materials on its
                Website or otherwise relating to such materials or any sites
                linked to this Website.
              </Typography>
              <Typography variant="h6" gutterBottom component="div">
                4. Limitations
              </Typography>
              <Typography variant="body1" gutterBottom component="div">
                Company Name or its suppliers will not be hold accountable for
                any damages that will arise with the use or inability to use the
                materials on Pomotivity Website, even if Company Name or an
                authorize representative of this Website has been notified,
                orally or written, of the possibility of such damage. Some
                jurisdiction does not allow limitations on implied warranties or
                limitations of liability for incidental damages, these
                limitations may not apply to you.
              </Typography>
              <Typography variant="h6" gutterBottom component="div">
                5. Revisions and Errata
              </Typography>
              <Typography variant="body1" gutterBottom component="div">
                The materials appearing on Pomotivity Website may include
                technical, typographical, or photographic errors. Company Name
                will not promise that any of the materials in this Website are
                accurate, complete, or current. Company Name may change the
                materials contained on its Website at any time without notice.
                Company Name does not make any commitment to update the
                materials.
              </Typography>
              <Typography variant="h6" gutterBottom component="div">
                6. Links
              </Typography>
              <Typography variant="body1" gutterBottom component="div">
                Company Name has not reviewed all of the sites linked to its
                Website and is not responsible for the contents of any such
                linked site. The presence of any link does not imply endorsement
                by Company Name of the site. The use of any linked website is at
                the user's own risk.
              </Typography>
              <Typography variant="h6" gutterBottom component="div">
                7. Site Terms of Use Modifications
              </Typography>
              <Typography variant="body1" gutterBottom component="div">
                Company Name may revise these Terms of Use for its Website at
                any time without prior notice. By using this Website, you are
                agreeing to be bound by the current version of these Terms and
                Conditions of Use.
              </Typography>
              <Typography variant="h6" gutterBottom component="div">
                8. Governing Law
              </Typography>
              <Typography variant="body1" gutterBottom component="div">
                Any claim related to Pomotivity Website shall be governed by the
                laws of Country without regards to its conflict of law
                provisions.
              </Typography>
            </DialogContentText>
          </DialogContent>
          <DialogActions>
            <Button onClick={handleCloseModal}>Cancel</Button>
            <Button
              variant="contained"
              color="primary"
              startIcon={<CheckIcon />}
              onClick={handleOnClickAcceptTerms}
            >
              I have read and agree to these rules
            </Button>
          </DialogActions>
        </Dialog>
      </div>
    );
  }
);
export default FormBody;
