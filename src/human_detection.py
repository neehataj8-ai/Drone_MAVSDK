import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO("models/yolo11n.pt")

# Open the default webcam (0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame.")
        break

    # Detect only humans (class 0)
    results = model(frame, classes=[0], conf=0.5)

    # Draw bounding boxes
    annotated_frame = results[0].plot()

    # Display the frame
    cv2.imshow("Human Detection", annotated_frame)

    # Exit on 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()