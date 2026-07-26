# Digital Twin of the SSP Building

A real-time Digital Twin of the **SSP Building** at the Faculty of Engineering, Alexandria University. This project combines IoT sensors, MQTT communication, and a software visualization platform to create a live virtual representation of the building.

The goal is to continuously collect environmental and operational data from the physical building, process it, and synchronize it with its digital counterpart. This enables users to monitor building conditions in real time while providing a scalable foundation for future smart-building applications such as energy management, predictive maintenance, and automated control.

---

## How It Works

The system follows a layered architecture that separates sensing, communication, processing, and visualization.

```text
┌───────────────────────────┐
│   Physical SSP Building   │
└─────────────┬─────────────┘
              │
              ▼
      IoT Sensor Network
              │
              ▼
      MQTT Publisher Nodes
              │
              ▼
         MQTT Broker
              │
              ▼
       MQTT subscriber Node
              │
              ▼
      Data Processing Layer
              │
              ▼
        Database storage
              │
              ▼
       Dashboard Interface
```

---

## System Components

### IoT Sensor Layer

The building is equipped with distributed IoT sensors that continuously collect real-world measurements.

Examples include:

* Temperature
* Humidity
* Air quality

Each sensor periodically generates a reading that represents the current state of a specific location within the building.

---

### Communication Layer

Sensor data is transmitted using the **MQTT (Message Queuing Telemetry Transport)** protocol.

MQTT was selected because it is:

* Lightweight
* Low bandwidth
* Event-driven
* Well suited for IoT applications

Instead of communicating directly with the software, sensors **publish** their readings to an MQTT broker.

The Digital Twin **subscribes** to the required topics and automatically receives every new measurement.

Example:

```text
Topic:
ssp/floor1/room204/temperature

Payload:
24.6
```

This publish/subscribe architecture decouples hardware from software, making the system easier to maintain and expand.

---

## Data Pipeline

Every sensor reading follows the same processing pipeline:

```text
Sensor Reading
      │
      ▼
Create MQTT Message
      │
      ▼
Publish to MQTT Broker
      │
      ▼
Digital Twin Subscriber
      │
      ▼
Data Processing
      │
      ▼
Update Digital Twin
```

The backend listens for incoming MQTT messages, parses the payload, validates the received values, and updates the corresponding building element within the digital twin.

---

## Software Architecture

The software is organized into independent modules, each with a single responsibility.

| Module                  | Responsibility                                     |
| ----------------------- | -------------------------------------------------- |
| **Sensor Nodes**        | Collect measurements from physical sensors         |
| **MQTT Publisher**      | Publishes sensor readings to the broker            |
| **MQTT Broker**         | Routes messages between publishers and subscribers |
| **MQTT Subscriber**     | Receives sensor data from subscribed topics        |
| **Processing Layer**    | Validates, parses, and organizes incoming data     |
| **Digital Twin Engine** | Updates the virtual representation of the building |
| **Visualization Layer** | Displays the building and its live sensor values   |

This modular architecture allows each component to be developed, tested, and extended independently.

---

## Technologies

* Python
* MQTT
* IoT Sensors
* Digital Twin Architecture
* Real-Time Data Streaming

---

## Design Principles

The project was designed around several key principles:

* **Modularity** – Each software component performs a single task.
* **Scalability** – New sensors and rooms can be added with minimal software changes.
* **Real-Time Synchronization** – The digital model continuously reflects the latest sensor readings.
* **Loose Coupling** – Hardware and software communicate only through MQTT, allowing either side to evolve independently.

By separating sensing, communication, processing, and visualization, the system provides a robust architecture that can grow from a monitoring platform into a complete smart-building management solution.
