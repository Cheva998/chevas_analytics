export function moveGauge(percentage) {
  const gaugeArc = 220;
    // The calculated angle from one extreme to the middle of the gauge in degrees
  const angleMiddleToTop = 120; 
  const gaugeIndicator = document.getElementById("colorIndicator");
  const needleIndicator = document.getElementById("needleIndicator");
  
  //const percentage = parseFloat(document.getElementById("slider").value);
  if (isNaN(percentage)) {
      throw new Error("Percentage must be a number");
  }
  if (percentage < 0 || percentage > 100) {
    throw new Error("Percentage must be a float number between 0 and 100");
  }
  const indicator = gaugeArc * percentage / 100;
  const angle = (2 * angleMiddleToTop * percentage / 100) - angleMiddleToTop;
  gaugeIndicator.style["stroke-dashoffset"] = gaugeArc - indicator;
  needleIndicator.style.transform = `rotate(${angle}deg)`
}