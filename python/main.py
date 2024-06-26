import cv2
import numpy as np
import pickle
import math
from BT_Demo import bluetooth



#from servo import ServoMotor
from angle import horizontal_angle,verticle_angle

# Load camera calibration data
with open("calib.pckl", "rb") as f:
    data = pickle.load(f)
    cMat = data[0]
    dcoeff = data[1]

# Initialize the video capture
cap = cv2.VideoCapture(0)

# Initializa BT
bt = bluetooth("   ")
while not bt.is_open():
  pass
print("BT Connected!")


# Set up ArUco dictionary and detector parameters
dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_7X7_100)
dt = cv2.aruco.DetectorParameters_create()

while True:
    ret, frame = cap.read()
    if not ret:
        break

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
            #print(int(corner[i][0]), int(corner[i][1]))
            cv2.putText(frame, f"({coord[0]}, {coord[1]})", coord, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        print(coord_vec)
        hor_angle = horizontal_angle(coord_vec, dist)
        ver_angle = verticle_angle(dist)

        # Display the distance to the marker
        cv2.putText(frame, f"Distance: {dist:.2f} cm", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        cv2.putText(frame, f"hor: {hor_angle:.2f}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        cv2.putText(frame, f"ver: {ver_angle:.2f}", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        # Send angle
        angle = 1000 * round(hor_angle) + ver_angle
        bt.write(angle)
        
        
        
# Show the frame
    cv2.imshow("Frame", frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()
