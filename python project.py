import cv2
import datetime
import pygame  

# Initialize pygame mixer
pygame.mixer.init()
# Load sound file
beep_sound = pygame.mixer.Sound("beep.wav")  # Make sure to provide the correct path to your sound file

# Open the webcam (0 for default webcam)
cap = cv2.VideoCapture(0)

# Read the first frame for background comparison
ret, frame1 = cap.read()
ret, frame2 = cap.read()

# Variable to track recording status and start time
recording = False
out = None
start_time = None

# Maximum recording time in seconds (2 minutes)
max_recording_duration = 2 * 60  # 2 minutes

while cap.isOpened():
    # Calculate the absolute difference between two frames
    diff = cv2.absdiff(frame1, frame2)

    # Convert the difference to grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply threshold to get binary image (motion areas are white)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # Dilate the threshold image to fill in the holes
    dilated = cv2.dilate(thresh, None, iterations=3)

    # Find contours (motion areas)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Detect if motion is detected by checking contour area
    motion_detected = False
    for contour in contours:
        if cv2.contourArea(contour) < 500:
            continue
        motion_detected = True
        # Draw rectangle around the detected motion
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display motion detection status
    if motion_detected:
        status_text = "Motion Detected!"
        beep_sound.play()  # Play beep sound when motion is detected
    else:
        status_text = "No Motion Detected"

    cv2.putText(frame1, status_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0 if motion_detected else 0), 2)

    # Start recording when motion is detected
    if motion_detected:
        if not recording:
            recording = True
            start_time = datetime.datetime.now()  # Record the start time
            # Generate file name with current timestamp
            filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".avi"
            # Define video codec and create VideoWriter object
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            out = cv2.VideoWriter(filename, fourcc, 20.0, (frame1.shape[1], frame1.shape[0]))
            print(f"Recording started: {filename}")

    # Write the current frame to video if recording
    if recording:
        out.write(frame1)

        # Check if 2 minutes have passed since the recording started
        elapsed_time = (datetime.datetime.now() - start_time).total_seconds()
        if elapsed_time >= max_recording_duration:
            print(f"Recording stopped after {max_recording_duration} seconds")
            recording = False
            out.release()

    # Display the frame
    cv2.imshow('Motion Detection', frame1)

    # Update frames for comparison
    frame1 = frame2
    ret, frame2 = cap.read()

    # Exit when 'q' key is pressed
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release webcam and close any open windows
cap.release()
if out is not None and recording:
    out.release()
cv2.destroyAllWindows()