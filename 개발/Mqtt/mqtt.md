# 라즈베리파이 >> PC mqtt 통신
라즈베리파이에서 정보를 수집하고, 해당 정보를 실시간으로 PC로 전송하는 과정을 구현

## mqtt 통신을 사용한 이유
#### 1.비동기 통신
- 장치나 서비스가 서로 계속 연결된 상태가 아니라 필요시에만 브로커를 통해서 메시지를 주고받기 때문에 **전력이 적게 소모**.
#### 2. 가볍고 효율적 
- 가볍고 단순한 프로토콜로, 네트워크 대역폭이 제한된 환경에서도 잘 작동하기 때문에 쓰레기통 용량과 같은 **간단한 데이터를 전송하는 데 매우 효과적**

#### 3. 유연한 구조
- 저희가 지금은 1개의 쓰레기통을 사용하지만, 실제 구현이 된다면 여러대의 쓰레기통이 **동시에** PC와 **통신**을 하게 되는데, MQTT는 **발행/구독(Pub/Sub)** 모델을 사용하므로, 여러 대의 장치가 동시에 데이터를 전공하거나 수신 가능
  
#### 4. 안정성과 QoS(메시지 전달의 신뢰성과 보증 수준)
- 다양한 품질 수준(QoS)을 제공하여 메시지가 **안정적**으로 전달 가능

` ※ QoS ? 발행자와 구독자 사이의 특정 메시지에 대한 전달 보증 수준을 정의`


  ---
# Raspberry Pi 코드 ( PC로 Data 보내는 코드) 
```python
import boto3
import picamera
import io
import time
import paho.mqtt.client as mqtt
import serial

def detect_text(photo_bytes):
    session = boto3.Session(
        aws_access_key_id='AKIART2CYAUWMHYDDSXX',
        aws_secret_access_key='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',
        region_name='ap-northeast-2'
    )
    client = session.client('rekognition')
   
    response = client.detect_text(Image={'Bytes': photo_bytes})

    textDetections = response['TextDetections']
    detected_texts = []
    for text in textDetections:
        if text['Type'] == 'WORD':
            detected_texts.append(text['DetectedText'])
   
    return detected_texts


def extract_lowest_number(text_list):
    lowest_number = float('inf')
    for text in text_list:
        try:
            number = int(text)
            lowest_number = min(lowest_number, number)
        except ValueError:
            pass
    return lowest_number

def send_to_mqtt(topic, message):
    client = mqtt.Client()
   
    client.connect("192.168.20.36 (라즈베리파이 IP 주소)", 1883, 60)
   
    client.publish(topic, message)

def send_to_arduino(arduino, data):
    arduino.write(data.encode())
   
   
def main():
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
   
    arduino = serial.Serial('/dev/ttyUSB0', 9600)

    while True:
        current_time = time.strftime(" %Y-%m-%d %H:%M:%S", time.localtime())
        print("현재 시간:", current_time)
       
        camera.start_preview()
        time.sleep(5)
       
        stream = io.BytesIO()
        camera.capture(stream, format='jpeg')
        photo_bytes = stream.getvalue()
       
        camera.stop_preview()
       
        detected_texts = detect_text(photo_bytes)
        
        print("Detected text\n----------")
        for text in detected_texts:
            print("검출된 텍스트:", text)

        lowest_number = extract_lowest_number(detected_texts)
        if lowest_number != float('inf'):
            # 만약, 숫자가 찍힐 경우 가장 낮은 숫자 출력
            print("가장 낮은 숫자:", lowest_number)
            # 아두이노에게 가장 작은 숫자 보내주기
            send_to_arduino(arduino, str(lowest_number))
           
        else:
            # 만약 숫자가 아무것도 인식되지 않을경우 FULL 로 인식
            lowest_number = "FULL"
            print("FULL") # FULL 출력
            send_to_arduino(arduino, '1') # 아두이노에게 '1'(출발) 신호보냄
           
        # PC에게 공백을 주고 lowest_number 1 current_time 순서대로 보내준다. 
        send_to_mqtt("hello/world", str(lowest_number)+" 1"+ current_time)
        time.sleep(5)

if __name__ == "__main__":
    main()
```

---
# PC 코드 (라즈베리파이에서 오는 data 받는 코드)
```python
import paho.mqtt.client as mqtt
import pymysql
import mysql.connector
import datetime

# Global 전역변수
data = None  

# mysql에 연결
db = mysql.connector.connect(host = 'project-db-stu3.smhrd.com',
                            port=3307,
                            user = 'Insa4_IOTA_hacksim_5',
                            password = 'aishcool5',
                            db = 'Insa4_IOTA_hacksim_5',
                            charset = 'utf8')

# 클라이언트와 connect
#Paho MQTT 라이브러리를 사용하여 특정 주제("hello/world")에 대해 구독하고 브로커와 연결
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("hello/world")  # Replace with your MQTT topic

# message 받기
# 메시지가 도착하면 on_message 함수가 호출
def on_message(client, userdata, msg):
    global data
    #그 안에서 받은 메시지를 전역 변수 data에 분리해서 저장
    print(f"Topic: {msg.topic}\nMessage: {msg.payload.decode()}")
    data = msg.payload.decode().split(' ')
    if data:
        # MySQL 데이터베이스와 연결을 맺고, 쿼리를 실행한 후 커밋하여 데이터를 확실하게 저장
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

            # BIN_COUNT, M_TIME, BIN_LEVEL 구성되어 있으며, 이를 분석해서 INSERT 
            cur.execute("INSERT INTO BIN_TEST(BIN_COUNT,M_TIME,BIN_LEVEL) VALUES (%s, %s, %s)", (ID, Time ,Bin_level))

            # 임시 저장된 형태로, 커밋을 이용해서 확실하게 저장해줘야함
            db.commit()

       

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Replace with your broker IP
client.connect("192.168.20.36", 1883, 60)  
# 영구 연결(메시지가 계속 도착할 수 있게 연결 유지)
client.loop_forever()

# DB를 모두 사용했다면 연결한 DB 닫아줘야함.
db.close() # mysql 워크벤치를 종료
```
