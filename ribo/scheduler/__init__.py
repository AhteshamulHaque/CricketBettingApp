from multiprocessing import Process
from adapter import RequestAdapter, ResponseAdapter
import time, os

class SchedulerProcess(Process):

    def __init__(self, pm, pn, ple):
        super().__init__(name='scheduler')
        self.pm = pm
        self.pn = pn
        self.ple = ple

        self.madapter = ResponseAdapter(self.pm)
        self.nadapter = RequestAdapter(self.pn)

    def run(self):
        while True:

            # poll for command from main
            mdata = self.madapter.get_command()
            if mdata:
                self.madapter.send_result('Response to main from scheduler')

            # poll for command from network
            ndata = self.nadapter.get_command()
            if ndata:
                self.nadapter.send_result('Response to network from scheduler')