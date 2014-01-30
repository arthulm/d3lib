import logging
import sys
 
class StreamToLogger(object):
   def __init__(self, logger, log_level=logging.INFO):
      self.logger = logger
      self.log_level = log_level
      self.linebuf = ''
 
   def write(self, buf):
      for line in buf.rstrip().splitlines():
         self.logger.log(self.log_level, line.rstrip())

def redirect(
   filename="out.log",
   filemode='a',
   level=logging.DEBUG,
   format='%(asctime)s:%(name)s:%(levelname)s:%(message)s',
   ):
    logging.basicConfig(level=level, format=format, filename=filename, filemode=filemode, )

    stdout_logger = logging.getLogger('STDOUT')
    sl = StreamToLogger(stdout_logger, logging.INFO)
    sys.stdout = sl

    stderr_logger = logging.getLogger('STDERR')
    sl = StreamToLogger(stderr_logger, logging.ERROR)
    sys.stderr = sl