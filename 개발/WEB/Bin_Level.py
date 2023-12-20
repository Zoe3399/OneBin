from flask import Flask, render_template, request, jsonify
import mysql.connector
import logging
import paho.mqtt.client as mqtt

app = Flask(__name__)
# logging.basicConfig(filename='error.log', level=logging.ERROR)

# # MySQL 연결 설정
db_config = {
    'host': 'project-db-stu3.smhrd.com',
    'port': 3307,
    'user': 'Insa4_IOTA_hacksim_5',
    'password': 'aishcool5',
    'database': 'Insa4_IOTA_hacksim_5',
}


# 쓰레기통 용량을 가져오는 함수
def get_trash_capacity():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(buffered=True)

        query = "SELECT BIN_LEVEL FROM BIN_INFO ORDER BY M_NUM DESC LIMIT 1"
        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            capacity = result[0]
        else:
            capacity = "N/A"

        cursor.close()
        conn.close()

        return capacity
    except mysql.connector.Error as err:
        logging.error(f"Error: {err}")  # 오류를 로그 파일에 기록
        return "Error"

# # 웹 페이지 라우트
@app.route("/")
def index():
    capacity = get_trash_capacity()
    return render_template("connect.html", capacity=capacity)  # 템플릿 파일 이름 변경

# MQTT 클라이언트 생성
mqtt_client = mqtt.Client()


# MQTT 브로커에 연결하는 콜백 함수
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


# MQTT 클라이언트에 콜백 함수 등록
mqtt_client.on_connect = on_connect

# MQTT 브로커에 연결
mqtt_broker_address = "broker.hivemq.com"
mqtt_port = 1883
mqtt_client.connect(mqtt_broker_address, mqtt_port, 60)

# MQTT 클라이언트 루프 실행
mqtt_client.loop_start()


# MQTT 메시지 발행 함수
def publish_mqtt_message(value):
    mqtt_client.publish("maple/world", str(value))

# 쓰레기통 출발 처리 함수
@app.route("/start", methods=["POST"])
def start_trash():
    try:
        publish_mqtt_message(1)
        return jsonify({"message": "쓰레기통 출발이 요청되었습니다."}), 200
    except Exception as e:
        return jsonify({"message": "쓰레기통 출발 요청을 실패했습니다."}), 500

# 쓰레기통 멈춤 처리 함수
@app.route("/stop", methods=["POST"])
def stop_trash():
    try:
        publish_mqtt_message(0)
        return jsonify({"message": "쓰레기통 멈춤이 요청되었습니다."}), 200
    except Exception as e:
        return jsonify({"message": "쓰레기통 멈춤 요청을 실패했습니다."}), 500

# ... (이후 코드와 동일)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)