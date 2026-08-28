from ultralytics import YOLO

class Detector:

    def __init__(self):

        self.model = YOLO("models/yolo11n.pt")

    def detect(self, frame):

        return self.model(
            frame,
            classes=[0],
            conf=0.5,
            verbose=False
        )