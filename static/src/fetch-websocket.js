import { moveGauge } from './gauge-script.js';
import { animateThermometer } from './thermometer-script.js';

document.addEventListener('DOMContentLoaded', function() {
    var socket = io();

    socket.on('value_update', function(data) {
        
        document.getElementById('temperature').textContent = data.temperature;
        document.getElementById('humidityValue').textContent = data.humidity;
        moveGauge(data.humidity);
        animateThermometer(data.temperature);
    })
})
