from machine import Pin
import utime

step = Pin(14, Pin.OUT)
direction = Pin(12, Pin.OUT)
enable = Pin(13, Pin.OUT)
led = Pin(2, Pin.OUT)

enable.off()
led.off()
direction.on()

motor_stepsize = 1.8 # degrees
microstepping = 16 # step multiplier, set by dip switches
step_size_eff = motor_stepsize/microstepping
step_size_eff = step_size_eff/(3*3*11.25) # include transmission
hrs_per_rev = 24 # earth revolves ones a day
step_interval = (3600*hrs_per_rev) / (360/step_size_eff)
print("Step Interval:", step_interval)

def stepOne(s=0.01):
  step.on()
  utime.sleep(s/2)
  step.off()
  utime.sleep(s/2)

def stepn(n, s=0.01):
    for i in range(n):
        if (i % 50) == 0:
            led.on()
        elif (i % 50) == 25:
            led.off()
        print(".", end="")
        stepOne(s)


direction.off()
stepn(500, 0.01)
direction.on()
stepn(500, 0.01)

while True:
    stepn(324000, step_interval)


