**1.First activate the envrioment:**
yolov7_tracking\Scripts\activate

**2.For the detecion:**

python detect_and_track1.py --weights (Add your pt file here) --source (video source for tracking) --no-trace --view-img --nosave --track --classes 4 --seed 2 --show-track --show-fps

**3.For change the color of track:**

--track-color

**4.For nobox and nolable:**

--nobbox --nolable

**5.For save:**

python detect_and_track1.py --weights IOCL_best.pt --source .\track.mp4 --no-trace --view-img  --track --classes 4 --seed 2 --show-track

**6.For increase thickness:**

--thickness
