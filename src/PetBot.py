import time
import logging
import threading

from Sensors import Distance
from Motion.Motion import Movement


class PetBot():
    def __init__(self):
        self.distance_sensor = Distance.Distance()
        self.movement = Movement()

    def init_sensors(self):
        self.distance_sensor.start_measuring()
        print "start sensors"

    def init_movement(self):
        self.movement.start_moving()
        pass

    def start(self):
        print "Starting bot"

        self.init_sensors()
        self.init_movement()

        while True:
            print "."
            time.sleep(.2)

    def stop(self):
        print "Stopping bot"
        return None
