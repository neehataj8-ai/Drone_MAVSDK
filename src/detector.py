from ultralytics import YOLO

class Detector:

    def __init__(self):
        print("Loading YOLO model...")

        self.model = YOLO("models/yolo11n.pt")

        print("YOLO Ready!")

    def detect(self, frame):

        results = self.model(
            frame,
            verbose=False
        )

        return results