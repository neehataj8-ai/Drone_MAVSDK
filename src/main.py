from camera import Camera
from detector import Detector
from tracker import Tracker
from target import TargetSelector
from distance import DistanceEstimator
from safety import SafetyAnalyzer
from visualizer import Visualizer
from logger import Logger
from gimbal import GimbalController

import cv2

SOURCE = 0   # Replace with RTSP URL on Jetson

camera = Camera(SOURCE)

detector = Detector()
tracker = Tracker()
selector = TargetSelector()
distance = DistanceEstimator()
safety = SafetyAnalyzer()
visualizer = Visualizer()
logger = Logger()
gimbal = GimbalController()

while True:

    success, frame = camera.read()

    if not success:
        break

    results = detector.detect(frame)

    people = tracker.update(results)

    for person in people:

        x1, y1, x2, y2 = person["box"]

        person["center"] = (
            (x1+x2)/2,
            (y1+y2)/2
        )

        person["distance"] = distance.estimate(person["box"])

    target = selector.select(people)

    gimbal.track(target)

    violations = safety.check(people)

    if violations:
        logger.log(f"Violations: {violations}")

    frame = visualizer.draw(frame, people, target)

    cv2.imshow("SAFE_DISTANCE_M", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()

cv2.destroyAllWindows()