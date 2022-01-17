import React from "react";
import Slider from "../Slider/Slider";
export default function Sliders({
  nSliders,
  currentActive,
  switchCustomerFunction,
}) {
  return (
    <div>
      {new Array(nSliders).fill(null).map((s, i) => (
        <Slider
          key={i}
          isActive={currentActive === i}
          onClick={() => switchCustomerFunction(i)}
        />
      ))}
    </div>
  );
}
