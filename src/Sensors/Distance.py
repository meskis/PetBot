import threading

import time


class Distance:
    distance = 0

    def __init__(self):
        self.thread = threading.Thread(name="Distance thread", target=self.start_thread)

    def __call__(self, *args, **kwargs):
        pass

    def get_distance(self):
        return self.distance

    def start_thread(self):
        while True:
            self.measure_distance()
            time.sleep(.05)
        pass

    def start_measuring(self):
        self.thread.start()

    def measure_distance(self):
        self.distance += 1
        pass
