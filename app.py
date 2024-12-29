from flask import Flask, request, jsonify

app = Flask(__name__)

# Хранилище для данных
sensor_data = []

@app.route('/data', methods=['POST'])
def receive_data():
    global sensor_data
    data = request.json  # Получаем JSON данные
    sensor_data.append(data)  # Добавляем данные в список
    return jsonify({"message": "Data received"}), 200

@app.route('/view', methods=['GET'])
def view_data():
    # Отображаем все данные
    return jsonify(sensor_data), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Работает на порту 5000
