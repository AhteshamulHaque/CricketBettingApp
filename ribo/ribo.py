from multiprocessing import Process, Pipe, Manager
from network import NetworkProcess
from scheduler import SchedulerProcess
from adapter import RequestAdapter, ResponseAdapter


class Ribo:

   def __init__(self, *args, **kwargs):

      self.pn = Pipe() # connected to network
      self.ps = Pipe() # connected to scheduler
      self.psn = Pipe() # network-scheduler connction pipe

      # these pipe list will only be updated by scheduler,
      # scheduler can maintains its own pipe list
      self.ple = Manager().list() # enforcer pipe list connected to main
      self.plen = Manager().list() # enforcer pipe list connected to network

      self.nproc = NetworkProcess(self.pn[1], self.psn[0], self.plen)
      self.sproc = SchedulerProcess(self.ps[1], self.psn[1], self.ple, self.plen)

      # adapter connected to network
      self.nadapter = RequestAdapter(self.pn[0])

      # adapter connected to scheduler
      self.sadapter = RequestAdapter(self.ps[0])


   def start_network(self):
      if not self.nproc.is_alive():
         try:
            self.nproc.start()
         except AssertionError:
            self.nproc = NetworkProcess(self.pn[1], self.psn, self.ple)
            self.nproc.start()


   def network_status(self):
      return self.nproc.is_alive()


   def stop_network(self):
      self.nproc.terminate()


   def get_scheduler_process(self):
      return self.sproc


   def start_scheduler(self):
      if not self.sproc.is_alive():
         try:
            self.sproc.start()
         except AssertionError:
            self.sproc = SchedulerProcess(self.ps[1], self.psn, self.ple)
            self.sproc.start()


   def scheduler_status(self):
      return self.sproc.is_alive()


   def stop_scheduler(self):
      self.sproc.terminate()


   def send_command_to_network(self, cmd):
      return self.nadapter.get_result(cmd)


   def send_command_to_scheduler(self, cmd):
      return self.sadapter.get_result(cmd)


if __name__ == '__main__':
   r = Ribo()