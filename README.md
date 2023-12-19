![header](https://capsule-render.vercel.app/api?type=waving&color=auto&height=100&section=header&fontSize=90)

# OneBin : One trash bin can change the world

## 💡 Analysis Topic 
Autonomous driving trash bins based on line tracing for automatic waste collection.

<br>

## 🔍 Background and Necessity of the Proposal
- In the context of waste management in large spaces such as airports, train stations, and shopping malls, there are challenges related to late-night operations, physical labor, and long waiting times. 
To address these issues, automating trash bin management can result in benefits such as reduced physical labor, manpower savings, and environmental improvements. 
Existing smart trash bins for households and businesses have limited functionality, whereas this product stands out with features like capacity data tracking and autonomous movement capabilities.

- Existing robotic vacuum cleaners have the functionality for automatic waste cleaning. However, when it comes to handling the large trash volumes in crowded places like airports and train stations, their effectiveness is limited.
  
- Compared to late-night labor, which has negative effects on the human body, utilizing this product 24/7 enables efficient environmental management of the entire airport with minimal workforce.

## 🔍 Analysis Objective
The goal of this project is to develop a system that utilizes autonomous driving technology in trash bins, allowing them to automatically return to designated collection points for emptying when they reach 100% capacity. This aims to create an efficient waste collection system and promote environmental protection.

<br>

## 💹 Domestic market size and current status of smart trash bins in South Korea.
- The current market size of smart trash bins in South Korea is primarily driven by smart trash bins for households. In larger facilities, such as commercial complexes, traditional trash bins are still managed manually to maintain cleanliness.

- Recently, robots have been introduced, and two robot vacuum cleaners are being operated at Incheon International Airport. However, this is being conducted as a pilot project. Airports experience a higher rate of trash generation due to passenger movements, resulting in faster turnover of trash bins compared to shopping malls. The amount of trash handled also varies depending on the size of the airport, indicating that the required quantity of smart trash bins may vary based on the facility's scale and nature.

## 📊 STP Strategy

#### Segmentation (시장 세분화) 
- It is expected to be classified as a type of B2B market. Rather than focusing on consumer preferences or needs, the strategy is to apply technology to mass-produce products and engage in business-to-business transactions.

#### Targeting (표적 시장)
- It is anticipated that sales and contracts will be targeted towards companies operating large facilities. In the case of airports or train stations, transparent disposal of trash bins is required, while in the case of complex shopping malls or large stores, aesthetics are emphasized, and products are expected to be produced and sold accordingly.

#### Positioning(포지셔닝)
- Due to the scarcity of existing products in the market, it is analyzed that a company needs a strategy to establish the brand's character and pursue specific features tailored to each sales outlet.
- ex) In the case of usage in airports or train stations, functionality and transparency inside the bins are emphasized rather than aesthetics.
- ex) In the case of usage in complex shopping malls or stores, aesthetics and ease of use are pursued.

<br>

## 📑 Overall Project Contents
We have developed a smart trash bin by attaching sensors inside the bin and connecting it to an autonomous RC car at the bottom of the bin. 
The smart trash bin utilizes a camera sensor inside the bin to transmit capacity information to a central computer. This information is then controlled manually or automatically to move the trash bin along a predetermined route.

#### 1. Utilizing a Raspberry Pi and AWS OCR library, the project measures the trash level using camera sensors.

#### 2. Line tracer sensors enable autonomous movement of the trash bins and their placement at specific collection points.

#### 3. The project establishes a communication structure using serial and MQTT protocols to communicate with the main computer.

#### 4. The main computer utilizes a responsive web application to manage the entire set of trash bins, providing real-time monitoring and control.

<br>

## 🛠 Tech Stack

1. WEB : HTML, CSS, Flask, Python, JavaScript
2. IOT : MQTT, Python, Arduino, RaspberryPi
3. DB : MySQL, MQTT, Flask
