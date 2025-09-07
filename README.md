# 🎛️ Traffic Light with Face Detection (Arduino + Python)

This is a small project that controls an RGB LED connected to an Arduino board using computer vision.  
A Python script detects faces from the webcam feed and sends commands to the Arduino over Serial.  

- ✅ If a **face is detected**, the LED turns **green**.  
- ❌ If **no face is detected**, the LED turns **red**.  

> ⚠️ This project is based on the tutorial from [Computer Vision Zone](https://www.computervision.zone/courses/computer-vision-arduino-chapter-1/).  
> All credits go to them — this repo simply collects the code and setup instructions in one place.

---

---

## 🔧 Dependencies

### Arduino
- Arduino IDE (tested with version 2.x)
- **[CVZone Arduino Library](https://drive.google.com/file/d/1oxaUi1p-jOvNoUtkEo825h8ego9dA22z/view?usp=share_link)**  
  Installation:
  1. Download the ZIP file.
  2. Open Arduino IDE → `Sketch` → `Include Library` → `Add .ZIP Library`.
  3. Select the downloaded file.

### Python
Make sure you have **Python 3.7+** installed.

Install the required packages:
```bash
pip install -r requirements.txt
