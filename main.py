from jetcam.csi_camera import CSICamera
import cv2
import time as time
import detect
import Jetson.GPIO as GPIO
import detect_pose
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
import duoji

flag = 0
new_image = 0
LED_Pin = 11
mask_flag = 0
give_mask_flag = 1
camera = CSICamera(capture_device=0, width=224, height=224)
camera.running = True
def callback(change):
    global new_image
    new_image = change['new']
    #cv2.imshow('res',new_image)
    
camera.observe(callback)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_Pin, GPIO.OUT)
i2c = busio.I2C(SCL, SDA)

pca = PCA9685(i2c)

pca.frequency = 50

#7号口输出PWM
servo11= servo.Servo(pca.channels[11],min_pulse=500, max_pulse=2500)
servo8 = servo.Servo(pca.channels[8],min_pulse=500, max_pulse=2500)
servo7 = servo.Servo(pca.channels[7],min_pulse=500, max_pulse=2500)
servo10 = servo.Servo(pca.channels[3],min_pulse=500, max_pulse=2500)

servo2 = servo.Servo(pca.channels[1],min_pulse=500, max_pulse=2500)


while (1):
    path = "image.jpg"
    cv2.imshow("CSI Camera0", new_image)
    cv2.imwrite(path, new_image)
    if flag == 0:
        opt = detect.parse_opt()
        res = detect.main(opt)

        if res == 'atypia':
            print('atypia')
            GPIO.output(LED_Pin, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(LED_Pin, GPIO.LOW)
            duoji.atypia()
            mask_flag = 1
        elif res == 'masking':
            print('masking')
            if mask_flag:
                duoji.shouhui()
                mask_flag = 0
            give_mask_flag = 1
            flag = 1
        elif res == 'unmasked':
            print('unmasked')
            GPIO.output(LED_Pin, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(LED_Pin, GPIO.LOW)
            if give_mask_flag:
                duoji.send()
                give_mask_flag = 0
            mask_flag = 1
        else:
            print('nothing')
    elif flag == 1:
        opt = detect_pose.parse_opt()
        res = detect_pose.main(opt)
        
        if res == 'special-gesture':
            print('special-gesture')
            GPIO.output(LED_Pin, GPIO.HIGH)
            time.sleep(5)
            GPIO.output(LED_Pin, GPIO.LOW)
            flag = 0
        elif res == 'none-gesture':
            print('none-gesture')
            flag = 0
        else:
            print('nothing')