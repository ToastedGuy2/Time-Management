import React from "react";
import Slider from "../Slider/Slider";
export default function Sliders({ nSliders, currentActive }) {
  return (
    <div>
      {new Array(nSliders).fill(null).map((s, i) => (
        <Slider key={i} isActive={currentActive - 1 === i} />
      ))}
    </div>
  );
}
