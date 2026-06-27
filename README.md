# Cyber-Physical Autonomous Safety Barrier (CP-ASB) for Smart Factories

An End-to-End Cyber-Physical System (CPS) designed to automate warehouse and factory floor safety. This system utilizes real-time computer vision tracking to detect safety zone breaches and actuate physical hardware containment under 150ms.

---

### 📌 Project Overview
Industrial automation in Japan (*Kaizen*) heavily prioritizes workplace safety (*Anzen Daiichi*). This project demonstrates a low-cost, low-latency solution to prevent accidents between human workers and Automated Guided Vehicles (AGVs) using edge intelligence.

---

### ⚙️ System Architecture & Data Pipeline
The system operates in a continuous, real-time sensing-to-actuation loop:
1. **Sensing:** The host computational unit captures 720p live video streams via an integrated webcam.
2. **Processing:** A local Python script processes frames in the HSV color space, running a masking algorithm to track predefined hazard indicators.
3. **Communication:** Upon crossing the pixel threshold, a low-latency data pipeline transmits trigger payloads (`b'1'` or `b'0'`) over a physical UART serial connection (USB).
4. **Actuation:** An Arduino microcontroller parses the payload, driving an active piezo alarm siren and micro-servo safety gate to isolate the danger zone.

---

### 🛠️ Tech Stack & Apparatus
* **Software Layers:** Python 3.x, OpenCV (Computer Vision Framework), PySerial (UART Communication Engine)
* **Hardware Infrastructure:** Arduino Uno, SG90 Servo Motor (Barrier Gate Actuator), 12V High-Output Piezo Electronic Siren
* **Communication Standard:** Universal Asynchronous Receiver-Transmitter (UART) Serial Protocol at 9600 Baud Rate

---

### 🚀 Implementation & Source Files
* `factory_safety.py`: Handles edge-based color space segmentation, threshold computations, and automated serial broadcasting.
* `factory_safety_firmware.ino`: Real-time embedded system firmware written in C++ to execute instant mechanical actuation based on software telemetry.

---

### 📈 Scalable Engineering Conclusions
By shifting computing tasks to local devices (Edge Computing), this architecture completely eliminates cloud network dependencies and latency bottlenecks. It serves as an accessible proof-of-concept for small and medium enterprises (SMEs) looking to optimize safety infrastructures without deploying expensive, heavy industrial hardware sensors.
