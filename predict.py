from ultralytics import YOLO

model = YOLO(r"C:\Users\cheta\Desktop\Chetan\ComputerVision\runs\detect\train13\weights\best.pt")

model.predict()