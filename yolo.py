from ultralytics import YOLO
import cv2

model = YOLO('yolov8l.pt')
results = model.train("train", show=True)

print(model.names)
