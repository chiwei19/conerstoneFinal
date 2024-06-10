from math import sqrt,atan,asin

frame_center = (640, 360)
k1 = 50
k2 = 200

def horizontal_angle(coord_vec, dist):
    # Compute angle between acuco and camera
    x_center = sum(corner[0] for corner in coord_vec) / 4
    y_center = sum(corner[1] for corner in coord_vec) / 4
    center = (x_center, y_center)
    #print(center)
    dr = sqrt((center[0] - frame_center[0]) ** 2 + (center[1] - frame_center[1]) ** 2)
    print(dr)
    hor_angle = atan((dr / k1)/ dist)
    print(hor_angle)
    return hor_angle

def verticle_angle(dist):
    ver_angle = 0.5 * asin(dist / k2)
    return ver_angle 
