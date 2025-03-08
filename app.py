from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit
#import board
#import adafruit_dht

pin = 11
#dht = adafruit_dht.DHT11(board.D4, use_pulseio=False)


import random
def get_temperature():
	#return dht.temperature
    return random.randrange(18, 28, 1)

def get_humidity():
	#return dht.humidity
    return random.randrange(20, 70, 2)

app = Flask(__name__)

socketio = SocketIO(app)

# Function to update the 
def send_updates():
    while True:
        temperature = get_temperature()
        humidity = get_humidity()
        socketio.emit('value_update', 
            {
                'temperature': temperature,
                'humidity': humidity
            })
        socketio.sleep(5)


@socketio.on('connect')
def handle_connect():
    #Send updates to this client
    socketio.start_background_task(send_updates)

# Define routes for web pages
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/app')
def app_page():
    return render_template('app.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Define routes for API
@app.route('/api/sensor_data', methods=['GET'])
def get_data():
    dataType = {'temperature': get_temperature, 'humidity': get_humidity}
    queryParams = request.args
    sensorType = queryParams.get('sensor_type')
    
    data = {sensorType: dataType[sensorType]()}
    return jsonify(data)

@app.route('/api/data', methods=['POST'])
def create_data():
    data = request.get_json()
    # Here you would typically save the data to a database or perform some action
    return jsonify({'message': 'Data created successfully!', 'data': data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
