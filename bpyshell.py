#!/usr/bin/env python

import sys, os
from EThread import EThread

THREADS=[]
LOGFILE="bpyshell_%s.log" % os.getpid()

def _initbpys(threads=[],start_threads=True):
    for t in threads:
        if callable(t):
          et = EThread(LOGFILE)
          et.__setattr__('_execute',type(et.__getattribute__('_execute'))(t,et))
          THREADS.append(EThread(t))
          if start_threads:
	      et.run()
    try:
        import bpython
        bpython.embed(locals())
    except AttributeError:
        print("Not started with `bpython` - no interactivity")

if __name__ == '__main__':
    _initbpys()