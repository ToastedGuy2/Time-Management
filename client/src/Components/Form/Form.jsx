import React, { useState } from "react";
import FormBody from "../FormBody/FormBody";
import FormFooter from "../FormFooter/FormFooter";
import FormHeader from "../FormHeader/FormHeader";

export default function Form() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [checked, setChecked] = useState(false);
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
  const handleSubmit = (event) => {
    event.preventDefault();
    console.log("Form Submitted");
  };
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
      />
      <FormFooter />
    </div>
  );
}
