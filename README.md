# RGB Light with Face Detection (Arduino + Python)

This is a small project that controls an RGB LED connected to an Arduino board using computer vision.  
A Python script detects faces from the webcam feed and sends commands to the Arduino over Serial.  

- ✅ If a **face is detected**, the LED turns **green**.  
- ❌ If **no face is detected**, the LED turns **red**.  

> ⚠️ Note: This project was built by following the tutorial from [Computer Vision Zone](https://www.computervision.zone/courses/computer-vision-arduino-chapter-1/).  
> The code structure is based on their course material, but I went through the process step by step to understand how Python communicates with Arduino.  
> This repo serves as my learning notes and a reference for anyone who wants to try the same project.
---
## Video:


https://github.com/user-attachments/assets/14e87eaa-6e79-487b-ab84-29b312ab63d5

---
## Schematics (KiCad):

![Face_Detection_RGBled](https://github.com/user-attachments/assets/3a760816-ea98-450e-9597-0e36619a0f9f)

---
## 🔧 Instructions

### Required components:
- Arduino UNO R3
- RGB Module HW-479 ( You can use other modules but make sure to check how to wire and its code )
- 4 Jumper wires

### Code:

#### Arduino:
- Arduino IDE (tested with version 2.x)
- **[CVZone Arduino Library](https://drive.google.com/file/d/1oxaUi1p-jOvNoUtkEo825h8ego9dA22z/view?usp=share_link)**  
  Installation:
  1. Download the ZIP file.
  2. Open Arduino IDE → `Sketch` → `Include Library` → `Add .ZIP Library`.
  3. Select the downloaded file.

#### Python:
Make sure you have **Python 3.7+** installed.

Install the required packages:
```bash
pip install cvzone
```
```bash
pip install opencv-python
```
```bash
pip install mediapipe
```


