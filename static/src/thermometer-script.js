export function animateThermometer(temperature) {
    const minY = 10;
    const maxY = 127;
    const tempRange = 100;

    // const temp = parseFloat(document.getElementById("slider").value);
    if (isNaN(temperature)) {
        throw new Error("Temperature must be a number");
    }
    if (temperature < 0 || temperature > 100) {
        throw new Error("Temperature must be a float between 0 and 100");
    }
    const thermometer = document.getElementById("rectMeter");
    let thermometerY = maxY - temperature * (maxY - minY) / tempRange;
    let thermometerHeight = temperature * (maxY - minY) / tempRange + 10;
    thermometer.setAttribute("y", thermometerY);
    thermometer.setAttribute("height", thermometerHeight);
}