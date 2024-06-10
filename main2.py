import cv2
import numpy as np
import pickle
from picamera2 import Picamera2
import time

# Load camera calibration data
with open("calib.pckl", "rb") as f:
    data = pickle.load(f)
    cMat = data[0]
    dcoeff = data[1]

# Initialize Picamera2
picam2 = Picamera2()
config = picam2.create_preview_configuration(main={"size": (640, 480)})  # Adjust size as needed
picam2.configure(config)
picam2.start()

# Set up ArUco dictionary and detector parameters
dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_7X7_100)
dt = cv2.aruco.DetectorParameters_create()

while True:
    # Capture a frame
    frame = picam2.capture()

    # Convert the frame to BGR format
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # Detect markers
    corners, ids, _ = cv2.aruco.detectMarkers(frame, dict, parameters=dt)

    if ids is not None and ids.size > 0:
        id = ids[0][0]
        corner = corners[0][0]

        # Estimate pose of the marker
        rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(corners[0], 0.05, cMat, dcoeff)
        dist = np.linalg.norm(tvec) * 100

        # Draw detected markers and coordinates
        cv2.aruco.drawDetectedMarkers(frame, corners)

        # Get and display the coordinates of the square
        coord_vec = []
        for i in range(len(corner)):
            coord = (int(corner[i][0]), int(corner[i][1]))
            coord_vec.append(coord)
            cv2.putText(frame, f"({coord[0]}, {coord[1]})", coord, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        hor_angle = horizontal_angle(coord_vec, dist)
        ver_angle = verticle_angle(dist)

        # Display the distance to the marker
        cv2.putText(frame, f"Distance: {dist:.2f} cm", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        cv2.putText(frame, f"hor: {hor_angle:.2f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        cv2.putText(frame, f"ver: {ver_angle:.2f}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    # Show the frame
    cv2.imshow("Frame", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release Picamera2 resources and close windows
picam2.stop()
cv2.destroyAllWindows()
