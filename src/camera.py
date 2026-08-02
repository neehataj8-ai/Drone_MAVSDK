import cv2

class Camera:

    def __init__(self):
        self.cap = cv2.VideoCapture("http://192.168.1.3:4747/video")

        if not self.cap.isOpened():
            raise Exception("Camera not found")

    def read(self):
        success, frame = self.cap.read()
        return success, frame

    def release(self):
        self.cap.release()