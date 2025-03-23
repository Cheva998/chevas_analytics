import { moveGauge } from './gauge-script.js';

document.addEventListener('DOMContentLoaded', function() {
    var socket = io();

    socket.on('value_update', function(data) {
        
        document.getElementById('temperature').textContent = data.temperature;
        document.getElementById('humidity').value = data.humidity;
        document.getElementById('humidityValue').textContent = data.humidity;
        moveGauge(data.humidity);
    })
})
