import detect
import Jetson.GPIO as GPIO
import time as time
from jetcam.csi_camera import CSICamera
import cv2
import os

camera0 = CSICamera(capture_device=0, width=224, height=224)
flag = 0
LED_Pin = 11
i = 1

while(1):
    path = "image"+str(i)+".jpg"
    image0 = camera0.read()
    #cv2.imshow("CSI Camera0", image0)
    cv2.imwrite(path, image0)
    kk = cv2.waitKey(1)
    if kk == ord('q'):  # 按下 q 键，退出
        break
    #opt = detect.parse_opt()
    #res = detect.main(opt)
    print(i)

    if res == 'atypia':
        print('atypia')
        #GPIO.setmode(GPIO.BOARD)
        #GPIO.output(LED_Pin, GPIO.HIGH)
        #time.sleep(2)
    elif res == 'masking':
        print('masking')
        flag = 1
    elif res == 'unmasked':
        print('unmasked')
        #GPIO.output(LED_Pin, GPIO.HIGH)
        #time.sleep(2)
    else:
        print('nothing')
    i = i+1
    #GPIO.cleanup()