from .EThread import EThread
import time

class PeriodicThread(EThread):
    def __init__(self,sleeptime,func=None,outstream=None):
        EThread.__init__(self,outstream)
        self._sleep=sleeptime
        self._periodicFunction = func

    def _execute(self):
        if self._periodicFunction != None:
            self._periodicFunction()
            time.sleep(self._sleep)

class PeriodicThread2(EThread):
    def __init__(self,sleeptime,func=None,outstream=None):
        EThread.__init__(self,outstream)
        self._sleep=sleeptime
        self._periodicFunction = func

    def _execute(self):
        if self._periodicFunction != None:
            self._periodicFunction(self)
            time.sleep(self._sleep)
