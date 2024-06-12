from math import sqrt,atan,asin

frame_center = (640, 360)
k1 = 70
k2 = 290

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
    return hor_angle * 180 / 3.14

def verticle_angle(dist):
    if  dist - 162 > 110 or dist - 162 < -110:
        ver_angle = 45
    else:
        ver_angle = (1.73 - 0.5 * asin((dist - 162 ) / 110)) * (180 / 3.14)
    
    return ver_angle
