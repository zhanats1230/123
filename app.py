from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Хранилище для данных
sensor_data = []

@app.route('/data', methods=['POST'])
def receive_data():
    global sensor_data
    # Получение данных от ESP32
    data = request.json
    data['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    sensor_data.append(data)
    return jsonify({"message": "Data received"}), 200

@app.route('/view', methods=['GET'])
def view_data():
    # Отображение данных
    return jsonify(sensor_data), 200

@app.route('/', methods=['GET'])
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>ESP32 Sensor Data</title>
        <meta charset="UTF-8">
    </head>
    <body>
        <h1>ESP32 Sensor Data</h1>
        <p>Visit <a href="/view">/view</a> to see the data.</p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
