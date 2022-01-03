import time
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

print('123')


i2c = busio.I2C(SCL, SDA)

pca = PCA9685(i2c)

pca.frequency = 50

#7号口输出PWM
servo11= servo.Servo(pca.channels[11],min_pulse=500, max_pulse=2500)
servo8 = servo.Servo(pca.channels[8],min_pulse=500, max_pulse=2500)
servo7 = servo.Servo(pca.channels[7],min_pulse=500, max_pulse=2500)
servo10 = servo.Servo(pca.channels[3],min_pulse=500, max_pulse=2500)

servo2 = servo.Servo(pca.channels[1],min_pulse=500, max_pulse=2500)

print('1')





def send():
    servo8.angle = 90
    servo2.angle = 90   
    servo10.angle = 1

    #舵机旋转角度
    servo11.angle = 90
    time.sleep(1)
    servo2.angle = 55
    time.sleep(1)
    servo7.angle = 179
    time.sleep(1)

    #time.sleep(5)

    time.sleep(1)
    servo8.angle = 160 #2

    time.sleep(1)
    servo10.angle=20

    print('21')
    time.sleep(3)
    servo2.angle = 90
    #time.sleep(1)
    print('口罩已夹起')


    time.sleep(1)
    servo10.angle=0
    time.sleep(1)
    servo8.angle = 90
    time.sleep(1)
    servo7.angle = 99
    time.sleep(3)
    servo2.angle = 55
    print('口罩已递出')
    

def shouhui():
    servo2.angle = 90
    time.sleep(1)
    servo10.angle = 1
    time.sleep(1)

    print('机械臂已收回')

def atypia():
    servo10.angle=20
    time.sleep(1)
    servo8.angle = 90
    time.sleep(1)
    servo7.angle = 99
    servo2.angle=55

pca.deinit()
