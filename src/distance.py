REAL_HEIGHT = 1.7
FOCAL_LENGTH = 700

class DistanceEstimator:

    def estimate(self, box):

        x1, y1, x2, y2 = box

        height = y2 - y1

        if height <= 0:
            return None

        return (REAL_HEIGHT * FOCAL_LENGTH) / height