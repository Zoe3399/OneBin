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
   
    client.connect("192.168.21.125", 1883, 60) #라즈베리파이 IP 주소
   
    client.publish(topic, message)

def send_to_arduino(arduino, data):
    arduino.write(data.encode())
   
   
def main():
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
   
    arduino = serial.Serial('/dev/ttyUSB0', 9600)

    while True:
        camera.start_preview()
        time.sleep(20)

        current_time = time.strftime(" %Y-%m-%d %H:%M:%S", time.localtime())
        print("현재 시간:", current_time)
       
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
        time.sleep(30)

if __name__ == "__main__":
    main()