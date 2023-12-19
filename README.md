![header](https://capsule-render.vercel.app/api?type=waving&color=auto&height=100&section=header&fontSize=90)

# OneBin : One trash bin can change the world

## 💡 Analysis Topic 

Autonomous driving trash bins based on line tracing for automatic waste collection.



## 🔍 Analysis Objective

The goal of this project is to develop a system that utilizes autonomous driving technology in trash bins, allowing them to automatically return to designated collection points for emptying when they reach 100% capacity. This aims to create an efficient waste collection system and promote environmental protection.



## 📑 Overall Project Contents

This project aims to efficiently manage waste disposal in large areas by automatically moving trash bins to designated collection points when they are full, based on sensor readings. Real-time data on the trash level and location of multiple bins is stored in a database, allowing for centralized control.

#### 1. Utilizing a Raspberry Pi and AWS OCR library, the project measures the trash level using camera sensors.

#### 2. Line tracer sensors enable autonomous movement of the trash bins and their placement at specific collection points.

#### 3. The project establishes a communication structure using serial and MQTT protocols to communicate with the main computer.

#### 4. The main computer utilizes a responsive web application to manage the entire set of trash bins, providing real-time monitoring and control.
---

### 🛠 Tech Stack

1. WEB : HTML, CSS, Flask, Python, JavaScript
2. IOT : MQTT, Python, Arduino, RaspberryPi
3. DB : MySQL, MQTT, Flask
