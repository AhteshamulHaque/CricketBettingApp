from multiprocessing import Process
from adapter import ResponseAdapter
import time, os

class NetworkProcess(Process):

    def __init__(self, pm, ps, ple):
        super().__init__(name='network')
        self.pm = pm
        self.ps = ps
        self.ple = ple

        self.madapter = ResponseAdapter(self.pm)
        self.sadapter = ResponseAdapter(self.pm)

    def run(self):
        while True:

            # poll for command from main
            mdata = self.madapter.get_command()
            if mdata:
                self.madapter.send_result('Response to main from network')

            # poll for command from scheduler
            sdata = self.sadapter.get_command()
            if sdata:
                self.sadapter.send_result('Response to scheduler from network')
            