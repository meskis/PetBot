import threading

import time


class Distance:
    distance = 0

    def __init__(self):
        self.stop_event = threading.Event()
        self.thread = threading.Thread(name="Distance thread", target=self.start_thread, args=(self.stop_event,))

    def __call__(self, *args, **kwargs):
        pass

    def get_distance(self):
        return self.distance

    def start_thread(self, stop_event):
        while not stop_event.wait(.05):
            self.measure_distance()

    def start_measuring(self):
        self.thread.start()

    def measure_distance(self):
        print 'measuring...'
        self.distance += 1

    def stop_measuring(self):
        print "stoppping distance module"
        self.stop_event.set()
