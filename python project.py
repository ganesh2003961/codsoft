import cv2
import datetime
import pygame  
pygame.mixer.init()
beep_sound = pygame.mixer.Sound("beep.wav") 
cap = cv2.VideoCapture(0)
ret, frame1 = cap.read()
ret, frame2 = cap.read()
recording = False
out = None
start_time = None
max_recording_duration = 2 * 60 
while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    motion_detected = False
    for contour in contours:
        if cv2.contourArea(contour) < 500:
            continue
        motion_detected = True
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
    if motion_detected:
        status_text = "Motion Detected!"
        beep_sound.play() 
    else:
        status_text = "No Motion Detected"
    cv2.putText(frame1, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0 if motion_detected else 0), 2)
    if motion_detected:
        if not recording:
            recording = True
            start_time = datetime.datetime.now()  # Record the start time
            filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".avi"
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(filename, fourcc, 20.0, (frame1.shape[1], frame1.shape[0]))
            print(f"Recording started: {filename}")
    if recording:
        out.write(frame1)
        elapsed_time = (datetime.datetime.now() - start_time).total_seconds()
        if elapsed_time >= max_recording_duration:
            print(f"Recording stopped after {max_recording_duration} seconds")
            recording = False
            out.release()
    cv2.imshow('Motion Detection', frame1)
    frame1 = frame2
    ret, frame2 = cap.read()
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
if out is not None and recording:
    out.release()
cv2.destroyAllWindows()
