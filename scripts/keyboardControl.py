from djitellopy import tello
import keyPressModule as kp
from time import sleep
import cv2

kp.init()

me = tello.Tello()
me.connect()
print(me.get_battery())
me.streamon() # to get the stream image

def getKeyboardInput():
    #left-right, foward-back, up-down, yaw veloity
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 30

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"): yv = speed
    elif kp.getKey("d"): yv = -speed

    if kp.getKey("e"): me.takeoff() # this allows the drone to takeoff
    if kp.getKey("q"): me.land() # this allows the drone to land

    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)

    img = me.get_frame_read().frame
    #img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)