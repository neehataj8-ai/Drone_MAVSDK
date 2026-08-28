from ultralytics import YOLO

model = YOLO("models/yolo11n.pt")

model.export(
    format="engine",
    imgsz=640,
    half=True
)