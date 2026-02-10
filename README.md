# MicroPython-servo
A simple MicroPython library for micro-servo.

## Features
- Easy to use.
- Compatible with EP32 and Raspberry.

## Example of use
```python
from servo import Servo
from time import sleep

'''---Creating the object servo with it's characteristics---'''
my_servo = Servo(pwm_pin=0, min_pulse_ms=0.5, max_pulse_ms=2.4, frequency=50)

'''---Movments---'''
for degree in [0, 45, 90, 135, 180]:
  my_servo.rotate(degree)
  sleep(1)
