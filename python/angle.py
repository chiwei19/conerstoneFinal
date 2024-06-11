from math import sqrt,atan,asin

frame_center = (640, 360)
k1 = 70
k2 = 200

def horizontal_angle(coord_vec, dist):
    # Compute angle between acuco and camera
    x_center = sum(corner[0] for corner in coord_vec) / 4
    y_center = sum(corner[1] for corner in coord_vec) / 4
    center = (x_center, y_center)
    #print(center)
    dr = (center[0] - frame_center[0])
    print(dr)
    hor_angle = asin((dr / k1)/ dist)
    print(hor_angle)
    return hor_angle * 180

def verticle_angle(dist):
    ver_angle = 0.5 * asin(dist / k2)
    return ver_angle * 180
