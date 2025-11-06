from ultralytics import YOLO
import cv2
import pytesseract
import numpy as np

# Tell pytesseract where to find the executable (change if installed elsewhere)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


class PlateReaderYOLO:
    def __init__(self, model_path="yolov8n.pt"):
        # You can replace this with a specialized license plate model if you have one
        self.model = YOLO(model_path)
        self.plate_memory = {}  # {track_id: plate_text}

    def detect_and_read(self, frame, tracks):
        annotated = frame.copy()

        for x1, y1, x2, y2, tid in tracks:
            # Crop the car ROI
            car_roi = frame[int(y1):int(y2), int(x1):int(x2)]

            # Detect smaller objects (potential plates) inside car region
            results = self.model.predict(car_roi, verbose=False, imgsz=320)
            for r in results:
                boxes = r.boxes.xyxy.cpu().numpy() if r.boxes is not None else []
                if len(boxes) == 0:
                    continue

                # Take the most confident small box as plate candidate
                for bx in boxes:
                    px1, py1, px2, py2 = bx[:4]
                    pw, ph = px2 - px1, py2 - py1

                    # Ignore large detections; plates are small
                    if pw < car_roi.shape[1] * 0.5 and ph < car_roi.shape[0] * 0.4:
                        plate_crop = car_roi[int(py1):int(py2), int(px1):int(px2)]
                        if plate_crop.size == 0:
                            continue

                        # OCR
                        gray = cv2.cvtColor(plate_crop, cv2.COLOR_BGR2GRAY)
                        gray = cv2.bilateralFilter(gray, 11, 17, 17)
                        text = pytesseract.image_to_string(gray, config='--psm 7')
                        text = ''.join(ch for ch in text if ch.isalnum())

                        # Store text persistently for this car
                        if text and len(text) >= 4:
                            self.plate_memory[tid] = text
                            cv2.rectangle(annotated, (int(x1), int(y1)), (int(x2), int(y2)), (255, 255, 0), 2)
                            cv2.putText(annotated, f"Plate: {text}", (int(x1), int(y2) + 25),
                                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
        return annotated
