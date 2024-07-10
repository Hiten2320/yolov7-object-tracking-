or activate the envrioment:
yolov7_tracking\Scripts\activate

for the detecion:
python detect_and_track1.py --weights (Add your pt file here) --source (video source for tracking) --no-trace --view-img --nosave --track --classes 4 --seed 2 --show-track --show-fps

for change the color of track:
--track-color

for nobox and nolable:
--nobbox --nolable

for save:
python detect_and_track1.py --weights IOCL_best.pt --source .\track.mp4 --no-trace --view-img  --track --classes 4 --seed 2 --show-track

for increase thickness
--thickness
