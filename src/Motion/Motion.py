import threading

import time


class Movement:
    speed = 0

    def __init__(self):
        self.stop_event = threading.Event()
        self.stop_event.clear()
        self.thread = threading.Thread(name="Movement thread", target=self.start_thread, args=(self.stop_event,))

    def __call__(self, *args, **kwargs):
        pass

    def start_thread(self, stop_event):
        print "Start driving"
        while not stop_event.wait(.1):
            print "Driving..."

    def start_moving(self):
        self.thread.start()

    def stop_moving(self):
        self.stop_event.set()
