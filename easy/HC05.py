import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 17
ECHO = 27

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def measure_distance():
    GPIO.output(TRIG, False)
    time.sleep(0.000002)  # slight settle time
    GPIO.output(TRIG, True)
    time.sleep(0.000010)  # 10 μs pulse
    GPIO.output(TRIG, False)

    # Wait for pulse to start
    start = time.time()
    timeout = start + 0.04  # ~ max 7 m. sensor spec ≈ 4 m but give safety margin
    while GPIO.input(ECHO) == 0 and time.time() < timeout:
        start = time.time()
    if time.time() >= timeout:
        return None  # timeout

    # Wait for pulse to end
    stop = time.time()
    timeout = stop + 0.04
    while GPIO.input(ECHO) == 1 and time.time() < timeout:
        stop = time.time()
    if time.time() >= timeout:
        return None  # timeout

    elapsed = stop - start
    distance_cm = round(elapsed * 17150, 2)  # sound speed conversion
    return distance_cm

try:
    while True:
        dist = measure_distance()
        if dist is None:
            print("Out of range / no echo")
        else:
            print(f"Distance: {dist} cm")
        time.sleep(0.2)

except KeyboardInterrupt:
    print("Great work done")
finally:
    GPIO.cleanup()
