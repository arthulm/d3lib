from threading import Thread
from sys import stdout

class EThread(Thread):
    """
     An extended thread class that is stopable (between runs of _execute()), has somewhat better readable output and startup(cleanSetup) and cleanup hooks.
     The action happens in _execute. This method should return periodically so that run() can chack if _runOK is still true.
    """
    def __init__(self, outstream=None):
        Thread.__init__(self)
        self._runOK = True
        if outstream is None:
            self._outstream = stdout
        else:
            self._outstream = outstream

    def __str__(self):
        return "%s@%s" % (self.__class__.__name__,self.getName())

    def _log(self, msg):
        self._outstream.write("[%s] %s\n" % (str(self),msg))

    def _cleanup(self):
        if not self.isAlive():
            raise Exception("This Thread already stoped!")

    def stop(self):
        self._runOK = False

    def run(self):
        while self._runOK:
            self._execute()
        self._cleanup()
