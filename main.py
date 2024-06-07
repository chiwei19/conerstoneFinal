import cv2
import numpy as np
import pickle

class ArucoDistanceCalculator:
    def __init__(self, calibration_file="calib.pckl", marker_size=0.05):
        with open(calibration_file, "rb") as f:
            data = pickle.load(f)
            self.cMat = data[0]
            self.dcoeff = data[1]
        self.marker_size = marker_size
        self.dict = cv2.aruco.Dictionary_get(cv2.aruco.DICT_7X7_100)
        self.dt = cv2.aruco.DetectorParameters_create()
    
    def calculate_distance(self, frame):
        corners, ids, _ = cv2.aruco.detectMarkers(frame, self.dict, parameters=self.dt)
        if ids is not None and ids.size > 0:
            corner = corners[0][0]
            rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(corners[0], self.marker_size, self.cMat, self.dcoeff)
            dist = np.linalg.norm(tvec)*100
            return dist
        else:
            return None

    def run(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            dist = self.calculate_distance(frame)
            if dist is not None:
                cv2.putText(frame, f"Distance: {dist:.2f} cm", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    distance_calculator = ArucoDistanceCalculator()
    distance_calculator.run()
