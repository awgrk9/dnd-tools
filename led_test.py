from rpi_hardware_pwm import HardwarePWM
import time

pwm = HardwarePWM(pwm_channel=0, hz=60)
pwm.start(0)
for i in range (101):
    pwm.change_duty_cycle(i)
    time.sleep(.1)
pwm.stop()

