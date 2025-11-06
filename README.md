
# 🚗 Vehicle Tracking and Speed Estimation System

A Python-based **Traffic Monitoring System** that detects and tracks vehicles in real-time video feeds using **YOLOv8**, **OpenCV**, and a **Simple Tracker (SORT-inspired)** algorithm.  
It also estimates each vehicle’s **speed** using frame-based displacement and FPS calibration.

---

## 🧠 Overview

This project is designed to simulate an **intelligent traffic monitoring system** capable of:
- Detecting vehicles in live or recorded video.
- Tracking each vehicle across frames.
- Estimating their speed in kilometers per hour.
- Displaying a visual ROI (region of interest) for focused analysis.

⚙️ Built with:
- **Python 3.13**
- **OpenCV** for video handling and visualization.
- **YOLOv8** for object detection.
- **Simple Tracker (SORT-based)** for ID persistence.
- **NumPy** for centroid/speed calculation.

---

## 📂 Project Structure
```
traffic-monitor/
│
├── main.py # main pipeline for detection, tracking & speed estimation
├── detector.py # handles YOLO-based vehicle detection
├── tracker.py # custom tracker for object ID management
├── speed_estimator.py # calculates pixel/frame speed
│
├── requirements.txt # all dependencies
└── README.md # this file
```


## 🚀 Features

✅ **Vehicle Detection** using YOLOv8  
✅ **Object Tracking** with persistent IDs  
✅ **Speed Estimation** in km/h  
✅ **Region of Interest (ROI)** overlay for clarity  
✅ **Optimized for 720p** video performance  
✅ **Lightweight and Modular Design**

---

## 🧩 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/vehicle-tracking-and-speed-estimation.git
cd vehicle-tracking-and-speed-estimation
```
### Install Dependencies
```bash
pip install -r requirements.txt
```
### Verify YOLO Installation
``` bash
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
```
## 🎥 Usage
### Run the main script
```bash
python main.py
```
### Adjust the main video
```bash
main("sample.mp4")
```
Replace "sample.mp4" with your own file path.

## ⚡ Performance Tips

If your video runs slower than expected, try the following optimizations:

### 🧩 1. Resize the video frames
High-resolution videos (e.g., 4K or 1080p) slow down YOLO and OpenCV.  
Resize frames before processing:
```python
frame = cv2.resize(frame, (1280, 720))
```
### ⚙️ 2. Skip frames (process every few frames)
You don’t need to analyze every single frame to maintain smooth tracking:
```python
frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_count += 1
    if frame_count % 3 != 0:
        continue  # Skip 2 out of every 3 frames
```
This improves performance up to 3× while keeping accuracy acceptable.



