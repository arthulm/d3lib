from threading import Thread
from sys import stdout

import RedirectedLogging

class EThread(Thread):
    """
     An extended thread class that is stopable (between runs of _execute()), has somewhat better readable output and startup(cleanSetup) and cleanup hooks.
     The action happens in _execute. This method should return periodically so that run() can chack if _runOK is still true.
    """
    def __init__(self, outstream=None):
        Thread.__init__(self)
        self._runOK = True
        self._outstream = outstream

    def __str__(self):
        return "%s@%s" % (self.__class__.__name__,self.getName())

    def _cleanup(self):
        if not self.isAlive():
            raise Exception("This Thread already stoped!")

    def stop(self):
        self._runOK = False

    def run(self):
        if self._outstream:
            RedirectedLogging.redirect(filename= self._outstream, format='%(asctime)s:'+str(self)+':%(name)s:%(levelname)s:%(message)s')
        while self._runOK:
            self._execute()
        self._cleanup()
