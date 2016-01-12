import os
import RPi.GPIO as GPIO
import time
import Controls

# ####################################
#               CONFIG
# ####################################

# car wheel pins

l_wheel1 = 11
l_wheel2 = 12
r_wheel1 = 13
r_wheel2 = 15

# Ultrasonic pins
ULTRA_TRIGGER = 38
# violet
ULTRA_ECHO = 40

GPIO.setwarnings(False)

# ----------- END OF CONFIG ----------

# -- TODO --
# variable speed

# ###################
#       SETUP
# ###################

FORWARD = 1
BACKWARD = 2

LEFT = 1
RIGHT = 2


def setup():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(l_wheel1, GPIO.OUT)
    GPIO.setup(l_wheel2, GPIO.OUT)
    GPIO.setup(r_wheel1, GPIO.OUT)
    GPIO.setup(r_wheel2, GPIO.OUT)
    GPIO.setup(ULTRA_TRIGGER, GPIO.OUT)
    GPIO.setup(ULTRA_ECHO, GPIO.IN)
    print "Init done."
    pass


def move(direction):
    print 'Starting to move...'

    if direction == FORWARD:
        print 'forward'
        GPIO.output(l_wheel1, True)
        GPIO.output(l_wheel2, False)
        GPIO.output(r_wheel1, True)
        GPIO.output(r_wheel2, False)
    else:
        print 'backward'
        GPIO.output(l_wheel1, False)
        GPIO.output(l_wheel2, True)
        GPIO.output(r_wheel1, False)
        GPIO.output(r_wheel2, True)


def turn(direction):
    print 'TURNING'

    if direction == LEFT:
        print 'LEFT'
        GPIO.output(l_wheel1, True)
        GPIO.output(l_wheel2, False)
        GPIO.output(r_wheel1, False)
        GPIO.output(r_wheel2, True)
    else:
        print 'RIGHT'
        GPIO.output(l_wheel1, False)
        GPIO.output(l_wheel2, True)
        GPIO.output(r_wheel1, True)
        GPIO.output(r_wheel2, False)

    time.sleep(.5)
    stop()


def stop():
    print 'stopping'
    GPIO.output(l_wheel1, False)
    GPIO.output(l_wheel2, False)
    GPIO.output(r_wheel1, False)
    GPIO.output(r_wheel2, False)


def get_raw_dist():
    GPIO.output(ULTRA_TRIGGER, False)
    print "Waitng For Sensor To Settle"
    time.sleep(.05)

    GPIO.output(ULTRA_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(ULTRA_TRIGGER, False)

    while GPIO.input(ULTRA_ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ULTRA_ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance, 2)  # Round to two decimal points

    print '--- DISTANCE: ' + distance.__str__() + ' ---'

    if distance > 2 and distance < 400:  # Check whether the distance is within range
        return distance - 0.5
    else:
        return 400


def get_distance():
    raw_dist1 = get_raw_dist()
    time.sleep(.05)
    raw_dist2 = get_raw_dist()
    time.sleep(.05)
    raw_dist3 = get_raw_dist()
    time.sleep(.05)
    raw_dist4 = get_raw_dist()

    dist = round((raw_dist1 + raw_dist2) / 2, 2)
    print "DIST: " + dist.__str__()

    return dist


# ----------- END OF SETUP ----------
setup()


def find_direction():
    stop()
    time.sleep(.2)
    turn(LEFT)
    time.sleep(.2)

    distance_on_left = get_distance()

    if distance_on_left < 20.0:
        turn(RIGHT)
        turn(RIGHT)

        distance_on_right = get_distance()

        if distance_on_left > distance_on_right:
            turn(LEFT)
            turn(LEFT)
            distance = distance_on_right
        else:
            distance = distance_on_left

        if distance < 20.0:
            move(BACKWARD)
            find_direction()

    return


straight_cycles = 0

while True:
    try:
        distance = get_distance()

        if distance < 20.0:
            move(BACKWARD)
            find_direction()

        print 'going forward'
        move(FORWARD)

        time.sleep(.1)

        if straight_cycles > 25:
            stop()
            move(BACKWARD)
            time.sleep(.5)
            stop()
            turn(RIGHT)
            time.sleep(.5)
            turn(RIGHT)
            time.sleep(.5)
            turn(RIGHT)
            straight_cycles = 0

        straight_cycles += 1

        print 'cycles done: ' + straight_cycles.__str__()

        print(chr(27) + "[2J")
        os.system('clear')

    except (KeyboardInterrupt, SystemExit):
        print '\nkeyboardinterrupt found!'
        print '\n...Program Stopped Manually!'
        GPIO.cleanup()
        raise
