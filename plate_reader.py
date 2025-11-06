import cv2
import pytesseract

# If Tesseract isn't in PATH, uncomment and set the path below
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class PlateReader:
    def __init__(self, cascade_path="haarcascade_russian_plate_number.xml"):
        # Load the OpenCV license plate detector
        self.plate_cascade = cv2.CascadeClassifier(cascade_path)

    def detect_and_read(self, frame, bbox):
        # Crop car region from bounding box
        x1, y1, x2, y2 = [int(v) for v in bbox]
        car_roi = frame[y1:y2, x1:x2]

        # Detect license plates within the car region
        plates = self.plate_cascade.detectMultiScale(car_roi, scaleFactor=1.1, minNeighbors=4)
        for (px, py, pw, ph) in plates:
            plate_roi = car_roi[py:py+ph, px:px+pw]

            # Convert to grayscale for better OCR
            gray_plate = cv2.cvtColor(plate_roi, cv2.COLOR_BGR2GRAY)
            # Optional: Apply thresholding for cleaner OCR
            gray_plate = cv2.bilateralFilter(gray_plate, 11, 17, 17)
            gray_plate = cv2.threshold(gray_plate, 150, 255, cv2.THRESH_BINARY)[1]

            # Read text with Tesseract
            text = pytesseract.image_to_string(gray_plate, config='--psm 7')
            return text.strip()  # Return the first detected plate

        # If no plates detected
        return None
