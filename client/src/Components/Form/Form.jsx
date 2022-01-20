import React, { useState, useEffect, useRef } from "react";
import FormBody from "../FormBody/FormBody";
import FormFooter from "../FormFooter/FormFooter";
import FormHeader from "../FormHeader/FormHeader";
import axios from "../../axios";
export default function Form() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [checked, setChecked] = useState(false);
  const [showModal, setShowModal] = useState(false);
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
      try {
        await axios.get(`/users?username=${username}`);
        await axios.post(`/users`, { username, password });
      } catch (error) {}
    }

    return () => {
      second;
    };
  }, [isRegisteringUser]);

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
