Digital Twin of the SSP Building – Faculty of Engineering, Alexandria University
Overview

This project implements a Digital Twin of the SSP Building at the Faculty of Engineering, Alexandria University. A digital twin is a software-based representation of a physical asset that continuously reflects its current state by receiving data from real-world sensors.

Unlike a traditional 3D model, a digital twin is dynamic. It is continuously updated with live information collected from the building, allowing users to monitor environmental conditions and building operations in real time. The software acts as a bridge between the physical building and its virtual counterpart, enabling visualization, monitoring, and future intelligent automation.

System Architecture

The system is composed of four independent layers that work together to transfer information from the building to the digital twin.

┌───────────────────────────────────────────┐
│              Physical Building            │
│      (SSP Faculty of Engineering)         │
└───────────────────────────────────────────┘
                    │
                    ▼
┌───────────────────────────────────────────┐
│              IoT Sensor Layer             │
│ Temperature │ Humidity │ Motion │ Light   │
│ Energy │ Air Quality │ Occupancy │ etc.   │
└───────────────────────────────────────────┘
                    │
                    ▼
┌───────────────────────────────────────────┐
│          MQTT Communication Layer         │
│     Publisher → Broker → Subscriber       │
└───────────────────────────────────────────┘
                    │
                    ▼
┌───────────────────────────────────────────┐
│         Data Processing Layer             │
│ Parsing │ Validation │ Formatting │ Logic │
└───────────────────────────────────────────┘
                    │
                    ▼
┌───────────────────────────────────────────┐
│          Digital Twin Application         │
│ Real-time Visualization & Monitoring      │
└───────────────────────────────────────────┘
