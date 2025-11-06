
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

