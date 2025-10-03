// This file does not execute, is an example only

const apiUrl = "api/sensor_data";

async function fetchSensorData(sensorType) {
    try {
        const response = await fetch(`${apiUrl}?sensor_type=${sensorType}`);
        if (!response.ok) {
            throw new Error(`HTTP error from sensor type: ${sensorType}.\
            Status code: ${response.status}`)
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error(`Error fetching ${sensorType} data: `, error);
        return null;
    }
}

async function fetchIotData() {
    try {
        const [tempData, humData] = await Promise.all([
            fetchSensorData('temperature'),
            fetchSensorData('humidity')
        ]);
        
        if (tempData) {
            document.getElementById('temperature').textContent = tempData.temperature;
            animateThermometer(tempData.temperature);
        }
        
        if (humData) {
            document.getElementById('humidity').value = humData.humidity;
            document.getElementById('humidityValue').textContent = humData.humidity;
            moveGauge(humData.humidity);
        }

    } catch (error) {
        console.error('Error fetching data: ', error);
    }
}

let humidity = 50; // Example humidity value

window.onload = fetchIotData;