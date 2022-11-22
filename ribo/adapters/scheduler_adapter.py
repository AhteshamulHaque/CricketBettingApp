
from multiprocessing import Queue
from scheduler import SchedulerProcess

class SchedulerAdapter:

   def __init__(self):
      self.__qs = Queue()