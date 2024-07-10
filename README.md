**1.First activate the envrioment:**
``` shell
yolov7_tracking\Scripts\activate
```

**2.For the detecion:**
``` shell
python detect_and_track1.py --weights (Add your pt file here) --source (video source for tracking) --no-trace --view-img --nosave --track --classes 4 --seed 2 --show-track --show-fps
```
**3.For change the color of track:**
``` shell
--track-color

```
**4.For nobox and nolable:**
``` shell
--nobbox --nolable
```
**5.For save:**
``` shell
python detect_and_track1.py --weights IOCL_best.pt --source .\track.mp4 --no-trace --view-img  --track --classes 4 --seed 2 --show-track

```
**6.For increase thickness:**
``` shell
--thickness
```
