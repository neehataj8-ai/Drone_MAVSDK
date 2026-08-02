from ultralytics import YOLO

# Load the model
model = YOLO("models/yolo11n.pt")

# Export to ONNX
success = model.export(format="onnx")

print("Export finished.")
print(success)