from gpiozero import PWMOutputDevice
import time

led = PWMOutputDevice(12)

led.value = 1
time.sleep(1)
led.value = 0.5
time.sleep(1)
led.value = 0
time.sleep(1)

try:
    while True:
        for duty_cycle in range (0,100,1):
            led.value = duty_cycle/100.0
            time.sleep(0.05)

        for duty_cycle in range(100,0,-1):
            led.value = duty_cycle/100.0
            time.sleep(0.05)

except KeyboardInterrupt:
    print("Stop the program")
    led.value = 0 
    pass



#pwm = HardwarePWM(pwm_channel=0, hz=60)
#pwm.start(0)
#for i in range (101):
#    pwm.change_duty_cycle(i)
#    time.sleep(.1)
#pwm.stop()

