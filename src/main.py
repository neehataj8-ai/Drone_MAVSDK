import cv2

from camera import Camera
from detector import Detector

camera = Camera()

detector = Detector()

while True:

    success, frame = camera.read()

    if not success:
        break

    results = detector.detect(frame)

    annotated_frame = results[0].plot()

    cv2.imshow("SAFE_DISTANCE_M", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()

cv2.destroyAllWindows()