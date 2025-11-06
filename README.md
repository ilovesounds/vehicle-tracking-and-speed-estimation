
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
traffic-monitor/
│
├── main.py # main pipeline for detection, tracking & speed estimation
├── detector.py # handles YOLO-based vehicle detection
├── tracker.py # custom tracker for object ID management
├── speed_estimator.py # calculates pixel/frame speed
│
├── requirements.txt # all dependencies
└── README.md # this file


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

