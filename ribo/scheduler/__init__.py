from multiprocessing import Process
from adapter import RequestAdapter, ResponseAdapter
import time, os

class SchedulerProcess(Process):

    def __init__(self, pm, pn, plen):
        super().__init__(name='scheduler')
        self.plen = plen # shared list scheduler - network for pipe
        self.madapter = ResponseAdapter(pm)
        self.nadapter = RequestAdapter(pn)

    def run(self):
        while True:

            # poll for command from main
            mdata = self.madapter.get_command()
            if mdata:
                self.madapter.send_result('Response to main from scheduler')