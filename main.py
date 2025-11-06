import cv2
from detector import VehicleDetector
from tracker import SimpleTracker
from speed_estimator import SpeedEstimator
from plate_reader_yolo import PlateReaderYOLO


def main(video_path):
    detector = VehicleDetector()
    tracker = SimpleTracker()
    plate_reader = PlateReaderYOLO()  # <-- using YOLO-based reader now

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"Video FPS: {fps}")

    speed_estimator = SpeedEstimator(fps)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (1280, 720))
        h, w, _ = frame.shape

        # Draw ROI (yellow)
        roi_y1, roi_y2 = int(h * 0.65), int(h * 0.95)
        cv2.rectangle(frame, (0, roi_y1), (w, roi_y2), (0, 255, 255), 2)

        # Vehicle detection + tracking
        detections = detector.detect(frame)
        tracks = tracker.update(detections)
        speeds = speed_estimator.estimate(tracks)

        # Draw boxes + speed
        for x1, y1, x2, y2, tid in tracks:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            speed = speeds.get(tid, 0)
            cv2.putText(frame, f"ID {tid} | {speed:.1f} km/h", (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

        # Run YOLO plate reader (draws persistent text)
        frame = plate_reader.detect_and_read(frame, tracks)

        cv2.imshow("Traffic Monitor", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main("sample.mp4")

