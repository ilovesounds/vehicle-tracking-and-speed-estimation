import numpy as np
from filterpy.kalman import KalmanFilter

class SimpleTracker:
    def __init__(self):
        self.tracks = {}
        self.next_id = 0

    def update(self, detections):
        new_tracks = {}
        tracked_boxes = []

        for det in detections:
            x1, y1, x2, y2, conf = det
            cx, cy = (x1 + x2) / 2, (y1 + y2) / 2

            best_id, best_dist = None, 50
            for tid, (px, py) in self.tracks.items():
                dist = np.linalg.norm([cx - px, cy - py])
                if dist < best_dist:
                    best_id, best_dist = tid, dist

            if best_id is not None:
                new_tracks[best_id] = (cx, cy)
                tracked_boxes.append((x1, y1, x2, y2, best_id))
            else:
                new_tracks[self.next_id] = (cx, cy)
                tracked_boxes.append((x1, y1, x2, y2, self.next_id))
                self.next_id += 1

        self.tracks = new_tracks
        return tracked_boxes
