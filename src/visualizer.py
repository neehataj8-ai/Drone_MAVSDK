import cv2

class Visualizer:

    def draw(self, frame, people, target):

        for person in people:

            x1, y1, x2, y2 = map(int, person["box"])

            color = (0,255,0)

            if person == target:
                color = (255,0,0)

            cv2.rectangle(
                frame,
                (x1,y1),
                (x2,y2),
                color,
                2
            )

        return frame