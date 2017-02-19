import RPi.GPIO as GPIO


class Controller:
    def __init__(self):
        pass

    # l_wheel1 = 0
    # l_wheel2 = 0
    # r_wheel1 = 0
    # r_wheel2 = 0
    #
    # def __init__(self, l_wheel1, l_wheel2, r_wheel1, r_wheel2):
    #     self.l_wheel1 = l_wheel1
    #     self.l_wheel2 = l_wheel2
    #     self.r_wheel1 = r_wheel1
    #     self.r_wheel2 = r_wheel2
    #
    #     print r_wheel2
    #     print self.r_wheel2
    #
    #     GPIO.setmode(GPIO.BOARD)
    #
    #     GPIO.setup(l_wheel1, GPIO.OUT)
    #     GPIO.setup(l_wheel2, GPIO.OUT)
    #     GPIO.setup(r_wheel1, GPIO.OUT)
    #     GPIO.setup(r_wheel2, GPIO.OUT)
    #
    #     print "Init done."
    #
    #     pass
    #
    # @classmethod
    # def stop(cls):
    #     print 'stopping...'
    #     GPIO.output(cls.l_wheel1, False)
    #     GPIO.output(cls.l_wheel2, False)
    #     GPIO.output(cls.r_wheel1, False)
    #     GPIO.output(cls.r_wheel2, False)
    #
    # @classmethod
    # def start(cls):
    #     print 'Starting to move...'
    #     print cls.l_wheel1
    #     print cls.l_wheel2
    #
    #     GPIO.output(cls.l_wheel1, True)
    #     GPIO.output(cls.l_wheel2, False)
    #     GPIO.output(cls.r_wheel1, True)
    #     GPIO.output(cls.r_wheel2, False)
    #
    # @classmethod
    # def turn_left(cls):
    #     print 'Turning left...'
    #
    # @classmethod
    # def turn_right(cls):
    #     print 'Turning right...'
    #
    #
    #
    #
    #     #
    #
    #     #
    #
    #     #
    #     # GPIO.output(l_wheel1, True)
    #     # GPIO.output(l_wheel2, False)
    #     # GPIO.output(r_wheel1, True)
    #     # GPIO.output(r_wheel2, False)
    #     #
    #     # time.sleep(1.5)
    #     #
    #     # GPIO.output(l_wheel1, False)
    #     # GPIO.output(l_wheel2, True)
    #     # GPIO.output(r_wheel1, False)
    #     # GPIO.output(r_wheel2, True)
    #     #
    #     # time.sleep(1.5)
