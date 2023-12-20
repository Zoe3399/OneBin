import paho.mqtt.client as mqtt
import pymysql
import mysql.connector
import datetime

data = None  # Global variable

db = mysql.connector.connect(host = 'project-db-stu3.smhrd.com',
                            port=3307,
                            user = 'Insa4_IOTA_hacksim_5',
                            password = 'aishcool5',
                            db = 'Insa4_IOTA_hacksim_5',
                            charset = 'utf8')

# 클라이언트와 connect
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("hello/world")  # Replace with your MQTT topic

# message 받기
def on_message(client, userdata, msg):
    global data
    print(f"Topic: {msg.topic}\nMessage: {msg.payload.decode()}")
    data = msg.payload.decode().split(' ')
    if data:
        with db.cursor() as cur:
            print(data)
            # 체크하려는 ID
            ID = int(data[1])
            print(ID)

            # 현재 시간
            # 여기서 에러발생
            Time = data[2]+' '+data[3]
            print(Time)

            # 쓰레기통 용량
            Bin_level = data[0]
            print(Bin_level)
            print()

            cur.execute("INSERT INTO BIN_INFO(BIN_COUNT,M_TIME,BIN_LEVEL) VALUES (%s, %s, %s)", (ID, Time ,Bin_level))

            # 임시 저장된 형태로, 커밋을 이용해서 확실하게 저장해줘야함
            db.commit()

       

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Replace with your broker IP
client.connect("broker.hivemq.com", 1883, 60)
client.loop_forever()

# DB를 모두 사용했다면 연결한 DB 닫아줘야함.
db.close() # mysql 워크벤치를 종료