import cv2

# Initialize the Haar Cascade classifier for human detection
human_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')

# Define the number of frames for loitering detection
LOITERING_FRAMES = 5

# Initialize the tracker dictionary
trackers = {}

# Initialize the loitering dictionary
loitering_dict = {}

# Function to detect humans in a frame
def detect_humans(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    humans = human_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return humans

# Function to start tracking a human
def start_tracker(frame, human):
    x, y, w, h = human
    tracker = cv2.TrackerKCF_create()
    tracker.init(frame, tuple(human))
    trackers[id(human)] = tracker
    loitering_dict[id(human)] = 0

# Function to update trackers and detect loitering
def update_trackers(frame):
    for tracker in list(trackers.values()):
        success, box = tracker.update(frame)
        if success:
            p1 = (int(box[0]), int(box[1]))
            p2 = (int(box[0] + box[2]), int(box[1] + box[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
            loitering_dict[id(tracker)] += 1
        else:
            del trackers[id(tracker)]
            del loitering_dict[id(tracker)]

# Function to check for loitering individuals
def check_loitering():
    for id_, count in list(loitering_dict.items()):
        if count >= LOITERING_FRAMES:
            print(f"Person with ID {id_} is loitering.")
            del loitering_dict[id_]

# Main function
def main():
    cap = cv2.VideoCapture("C:\\Users\\hiten\\Desktop\\loitering\\MFF_WEST_BEAM_SHOP_BS_CAM8_20240216083025_20240216083340_550636.mp4")
    if not cap.isOpened():
        print("Error: Unable to open video file.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        humans = detect_humans(frame)

        for human in humans:
            if id(human) not in trackers:
                start_tracker(frame, human)

        update_trackers(frame)
        check_loitering()

        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Entry point of the script
if __name__ == "__main__":
    main()
