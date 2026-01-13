# Card prediction
Little yolo project in order to just play with it. The purpose of this project is to do live inference to detect playing cards. It was a nice little dataset I found from Kaggle

# Data
Got it from:
https://www.kaggle.com/datasets/artemzysko/playing-cards-dataset-yolo-object-detection/data

Might need a different dataset though or some additional ones

# Train-Val split
We split the data using "train_val_split.py", it's quite simple actually. The relevant arguments are "train_percent" and "data_path". For more info read the file itself, it's actually suprisingly well documented.

# Config file
Make sure to adjust config file for different projects!!!
It's the data.yaml file

# Training
Training is quite simple actually. There is no script for it, instead we can just train using the functionality provide by ultralytics CLI.
https://docs.ultralytics.com/usage/cli/

In our case we run (in the terminal):
yolo detect train data=data.yaml model=yolov8n.pt epochs=60 imgsz=640 batch=16

Note: 
1. lowered batch size because of the small vram on gpu
2. for the same reason picked one of the smaller models

To see more details we can run:
yolo

Lastly, to see all the available configs run:
yolo cfg

# What if I crash during training???
In case of a crash (which occured frequently do to limited vram) we can continue with:
yolo detect train resume=True model=runs/detect/train/weights/last.pt

(where runs/detect/train/weights/last.pt is the specific path of the latest run, but it could be different, just ensure that you use the correct path! I'm just showing an example for future me)

# Live inference
We can also do this through the CLI. We want to use the webcam so we set source=0. Additionally we'd like to show the predictions live, so we set show=True. Lastly, we are interested in only the predictions with high confidence and hence set conf=0.7.
yolo detect predict model=runs/detect/train3/weights/best.pt source=0 show=True conf=0.80


# Additional notes
Running into the issue that I can't load + train bigger models, so I'm fairly limited by my hardware. Should get back to this project after I get myself a fancy smacy new computer. Current conclusion is that it's fairly possible, and that it already shows great promise. 

Might be able to obtain better preformance by including additional data, or by performing some additional augmentations. The model performs fairly well on the validation set, so it might just be that my cards/environment is not accurately captured by the data (both train and val). Maybe try again but only with data manually collected + annotated based on my cards in my environment. (Probably per card 30 instances, in different lighting) Could also try a combination of both data sets.