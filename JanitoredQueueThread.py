from .QueueThread import QueueThread
from queue import Empty
from datetime import datetime,timedelta

class JanitoredQueueThread(QueueThread):
    def __init__(self,timeout,maxsize=0):
        QueueThread.__init__(self,maxsize)
        self._timeout=timeout

    def janitor(self):
        pass

    def _execute(self):
        cycle_end = datetime.now() + timedelta(seconds=self._timeout)
        while True:
            timeout = (cycle_end - datetime.now()).total_seconds()
            try:
                self._process(self.get(True,timeout))
                self.task_done()
            except Empty as e:
                pass
            if datetime.now() >= cycle_end:
                break
        self.janitor()
