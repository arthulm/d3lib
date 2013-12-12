from .EThread import EThread
from queue import Queue,Empty

import time

class QueueThread(EThread,Queue):
    def __init__(self,maxsize=0,autoSetup=True, outstream=None):
        Queue.__init__(self,maxsize)
        EThread.__init__(self, outstream)
        self._queueWait = 1
        self._retryWait = 5
        if autoSetup:
            try:
                self._cleanSetup()
            except Exception as e:
                self._log(e)

    def _cleanSetup(self, error=None):
        pass

    def _process(self, e):
        self._log("processing: %s" % str(e))

    def _execute(self):
        try:
            element = self.get(True,self._queueWait)
        except Empty:
            element = None
        while element != None:
            try:
                self._process(element)
                self.task_done()
                element = None
            except Exception as e:
                self._log(e)
                retry = True
                while retry:
                    try:
                        self._cleanSetup(e)
                        retry = False #stop retrying if cleanSetup does not raises errors
                    except Exception as e2:
                        self._log("error on cleanSetup: %s" % e2)
                        time.sleep(self._retryWait) #wait to retry
