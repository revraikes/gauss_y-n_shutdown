from sense_hat import SenseHat, ACTION_PRESSED
import time
import math
import os

sense = SenseHat()
sense.low_light = True
sense.clear()

R = (255, 0, 0)
G = (0, 255, 0)
Y = (255, 255, 0)
B = (0, 0, 0)

threshold = 55.0

def get_magnetic_strength():
    mag = sense.get_compass_raw()
    x = mag['x']
    y = mag['y']
    z = mag['z']
    strength = math.sqrt(x**2 + y**2 + z**2)
    return strength
    
#gaussmeter
def mag_strength():
    strength = get_magnetic_strength()
    print(f"Mag Field Strength: {strength:.2f} µT")
    if strength > threshold:
        color = R
    else:
        color = G
    sense.clear(color)
    time.sleep(.05)
    
alive = [
    B, B, Y, Y, Y, Y, B, B,
    B, Y, B, B, B, B, Y, B,
    Y, B, B, Y, Y, B, B, Y,
    Y, B, Y, B, B, Y, B, Y,
    Y, B, B, B, B, B, B, Y,
    Y, B, Y, B, B, Y, B, Y,
    B, Y, B, B, B, B, Y, B,
    B, B, Y, Y, Y, Y, B, B
]

dead = [
    R, B, B, B, B, B, B, R,
    B, R, B, B, B, B, R, B,
    B, B, R, R, R, R, B, B,
    B, B, B, B, B, B, B, B,
    R, B, R, B, B, R, B, R,
    B, R, B, B, B, B, R, B,
    R, B, R, B, B, R, B, R,
    B, B, B, B, B, B, B, B
]

def pushed_in(event):
    if event.action == ACTION_PRESSED:
        for _ in range(500):
            mag_strength()
        sense.clear()
        
def pushed_out(event):
    if event.action == ACTION_PRESSED:
        sense.clear()
        
def pushed_eth(event):
    if event.action == ACTION_PRESSED:
        sense.set_pixels(alive)
        
def pushed_pwr(event):
    if event.action == ACTION_PRESSED:
        sense.set_pixels(dead)

def pushed_ctr(event):
    if event.action == ACTION_PRESSED:
        os.system("sudo shutdown -h now")

def wait_for_joy():
    for event in sense.stick.get_events():
        return event.direction
        
sense.stick.direction_up = pushed_in
sense.stick.direction_down = pushed_out
sense.stick.direction_right = pushed_eth
sense.stick.direction_left = pushed_pwr
sense.stick.direction_middle = pushed_ctr

while True:
    pass
