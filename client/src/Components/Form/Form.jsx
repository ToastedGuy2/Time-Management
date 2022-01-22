import React, { useState, useEffect, useRef } from "react";
import FormBody from "../FormBody/FormBody";
import FormFooter from "../FormFooter/FormFooter";
import FormHeader from "../FormHeader/FormHeader";
import axios from "../../axios";
import { Typography } from "@mui/material";
const get_user_by_username = (username) => axios.get(`/users/${username}`);
const create_user = (username, password) =>
  axios.post(`/users`, { username, password });
export default function Form() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [checked, setChecked] = useState(false);
  const [showModal, setShowModal] = useState(false);
  const [isDone, setIsDone] = useState(false);
  const [usernameError, setUsernameError] = useState({
    error: false,
    errorMessage: "This field is required",
  });
  const [passwordError, setPasswordError] = useState({
    error: false,
    errorMessage: "This field is required",
  });
  const [checkboxError, setCheckboxError] = useState({
    error: false,
    errorMessage: "This field is required",
  });
  const [isRegisteringUser, setIsRegisteringUser] = useState(false);
  const [showAlert, setShowAlert] = useState(false);
  const handleClickShowPassword = () => {
    setShowPassword(!showPassword);
  };
  const usernameHandle = (evt) => {
    setUsername(evt.currentTarget.value);
  };
  const passwordHandle = (evt) => {
    setPassword(evt.currentTarget.value);
  };
  const handleClickOnCheckbox = () => {
    setChecked(!checked);
  };
  const handleOpenModal = () => {
    if (!isRegisteringUser) {
      setShowModal(true);
    }
  };

  const handleCloseModal = () => {
    setShowModal(false);
  };
  const handleOnClickAcceptTerms = () => {
    setChecked(true);
    setShowModal(false);
  };
  const openAlert = () => {
    setShowAlert(true);
  };
  const closeAlert = () => {
    setShowAlert(false);
  };
  const isStringEmpty = (value) => !value || value.trim().length === 0;
  const startRegisteringUser = () => {
    setIsRegisteringUser(true);
  };
  const finishedRegisteringUser = () => {
    setIsRegisteringUser(false);
    isDone();
  };
  const handleSubmit = (event) => {
    event.preventDefault();
    let isFormOkay = true;
    if (isStringEmpty(username)) {
      setUsernameError({ ...usernameError, error: true });
      isFormOkay = false;
    } else {
      setUsernameError({ ...usernameError, error: false });
    }
    if (isStringEmpty(password)) {
      setPasswordError({ ...passwordError, error: true });
      isFormOkay = false;
    } else {
      setPasswordError({ ...passwordError, error: false });
    }
    if (checked) {
      setCheckboxError({ ...checkboxError, error: false });
    } else {
      setCheckboxError({ ...checkboxError, error: true });
      isFormOkay = false;
    }
    if (isFormOkay) {
      startRegisteringUser();
    }
  };
  const ref = useRef(null);
  const insert_user = async () => {
    try {
      await get_user_by_username(username);
      await create_user(username, password);
      finishedRegisteringUser();
      setIsDone(true);
    } catch (error) {
      const { data, status, headers } = error.response;
      if (status === 404) {
        setUsernameError({
          error: true,
          errorMessage: "Username already exist.",
        });
      }
      if (status === 500) {
        openAlert(true);
      }
      finishedRegisteringUser();
    }
  };
  useEffect(() => {
    if (showModal) {
      const { current: descriptionElement } = ref;
      if (descriptionElement !== null) {
        descriptionElement.focus();
      }
    }
  }, [showModal]);
  useEffect(() => {
    if (isRegisteringUser) {
      insert_user();
    }

    // return () => {
    //   setIsRegisteringUser(false);
    // };
  }, [isRegisteringUser]);

  if (isDone) {
    return (
      <Typography variant="h1" color="initial">
        Hello World
      </Typography>
    );
  }
  return (
    <div>
      <FormHeader title="Welcome" />
      <FormBody
        username={username}
        password={password}
        usernameInputOnChange={usernameHandle}
        passwordInputOnChange={passwordHandle}
        handleClickShowPassword={handleClickShowPassword}
        showPassword={showPassword}
        checked={checked}
        handleClickOnCheckbox={handleClickOnCheckbox}
        handleSubmit={handleSubmit}
        ref={ref}
        showModal={showModal}
        handleOpenModal={handleOpenModal}
        handleCloseModal={handleCloseModal}
        handleOnClickAcceptTerms={handleOnClickAcceptTerms}
        usernameError={usernameError}
        passwordError={passwordError}
        checkboxError={checkboxError}
        isRegisteringUser={isRegisteringUser}
        showAlert={showAlert}
        handleCloseAlert={closeAlert}
      />
      <FormFooter />
    </div>
  );
}
