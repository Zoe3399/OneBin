![header](https://capsule-render.vercel.app/api?type=waving&color=auto&height=100&section=header&fontSize=90)

# OneBin : One trash bin can change the world

## 💡 Analysis Topic 
Autonomous driving trash bins based on line tracing for automatic waste collection.

## 🔍 Background and Necessity of the Proposal
- In the context of waste management in large spaces such as airports, train stations, and shopping malls, there are challenges related to late-night operations, physical labor, and long waiting times. 
To address these issues, automating trash bin management can result in benefits such as reduced physical labor, manpower savings, and environmental improvements. 
Existing smart trash bins for households and businesses have limited functionality, whereas this product stands out with features like capacity data tracking and autonomous movement capabilities.

- Existing robotic vacuum cleaners have the functionality for automatic waste cleaning. However, when it comes to handling the large trash volumes in crowded places like airports and train stations, their effectiveness is limited.
  
- Compared to late-night labor, which has negative effects on the human body, utilizing this product 24/7 enables efficient environmental management of the entire airport with minimal workforce.

## 🔍 Analysis Objective
The goal of this project is to develop a system that utilizes autonomous driving technology in trash bins, allowing them to automatically return to designated collection points for emptying when they reach 100% capacity. This aims to create an efficient waste collection system and promote environmental protection.

=
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
