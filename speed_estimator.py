import math

class SpeedEstimator:
    def __init__(self, fps, pixel_to_meter=0.04):
        self.fps = fps
        self.pixel_to_meter = pixel_to_meter
        self.last_positions = {}

    def estimate(self, tracks):
        speeds = {}
        for x1, y1, x2, y2, tid in tracks:
            cx, cy = (x1 + x2) / 2, (y1 + y2) / 2

            if tid in self.last_positions:
                px, py = self.last_positions[tid]
                dist_pixels = math.sqrt((cx - px) ** 2 + (cy - py) ** 2)
                speed_m_per_s = dist_pixels * self.fps * self.pixel_to_meter
                speed_kmh = speed_m_per_s * 3.6
                speeds[tid] = round(speed_kmh, 1)
            else:
                speeds[tid] = 0.0

            self.last_positions[tid] = (cx, cy)

        return speeds
