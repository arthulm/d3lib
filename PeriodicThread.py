from threading import Thread
import time

class PeriodicTread(Thread):
    def __init__(self,sleeptime,func=None):
        Thread.__init__(self)
        self._sleep=sleeptime
        self._periodicFunction = func

    def _proc(self):
        if self._periodicFunction != None:
            self._periodicFunction()

    def run(self):
        self.runOK=True
        while self.runOK:
            self._proc()
            time.sleep(self._sleep)

