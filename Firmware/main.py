from machine import Pin
import utime

step = Pin(14, Pin.OUT)
direction = Pin(12, Pin.OUT)
enable = Pin(13, Pin.OUT)
led = Pin(2, Pin.OUT)

enable.off()

direction.on()

def stepOne(s=0.01):
  step.on()
  led.on()
  utime.sleep(s)
  step.off()
  led.off()
  utime.sleep(s)

def stepn(n, s=0.01):
    for _ in range(n):
        print(".", end="")
        stepOne(s)

# This is for 1.8 degree stepper motors
while True:
    stepn(100, 132.91)


