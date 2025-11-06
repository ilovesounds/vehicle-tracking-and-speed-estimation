from ultralytics import YOLO
import cv2

model = YOLO("keremberke/yolov8n-license-plate-detection")

frame = cv2.imread("car.jpeg")  # put a clear image of a car with visible plate
results = model(frame, show=True)
cv2.waitKey(0)
