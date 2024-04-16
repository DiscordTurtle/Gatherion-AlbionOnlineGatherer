from ultralytics import YOLO
from train_test_split import train_test_split
import time

#train_test_split()

#time.sleep(1)

model = YOLO('yolov5n.yaml') 


results = model.train(data = "models/configuration.yaml", epochs = 1)


