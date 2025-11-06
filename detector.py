from ultralytics import YOLO
import numpy as np

class VehicleDetector:
    def __init__(self, model="yolov8m.pt"):
        self.model = YOLO(model)
        self.allowed = {"car", "bus", "truck", "motorbike"}

    def detect(self, frame):
        # Focus on middle + bottom area of the frame (ignore top trees/sky)
        h, w, _ = frame.shape
        y1, y2 = int(h * 0.35), int(h * 0.95)  # adjust if needed
        roi = frame[y1:y2, :]  # only the bottom 60% of the frame

        results = self.model(roi, verbose=False, conf=0.15)
        detections = []
        for r in results:
            for box in r.boxes:
                cls_name = self.model.names[int(box.cls)]
                if cls_name in self.allowed:
                    x1, y1b, x2, y2b = box.xyxy[0]
                    conf = float(box.conf[0])
                    # shift coordinates back to original frame
                    detections.append([x1.item(), y1b.item() + y1, x2.item(), y2b.item() + y1, conf])
        return np.array(detections)

