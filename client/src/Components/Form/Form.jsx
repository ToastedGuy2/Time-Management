import React from "react";
import FormBody from "../FormBody/FormBody";
import FormFooter from "../FormFooter/FormFooter";
import FormHeader from "../FormHeader/FormHeader";

export default function Form() {
  return (
    <div>
      <FormHeader title="Welcome" />
      <FormBody />
      <FormFooter />
    </div>
  );
}
