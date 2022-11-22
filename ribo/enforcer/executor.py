class EnforcerProcess(Process):

   def __init__(self, ps, pn, t):
      super().__init__(name='enforcer')
      self.sadapter = ResponseAdapter(ps)
      self.nadapter = RequestAdapter(pn)
      self.enforcer = enforcer[t]

   def run(self):
      while True:

         # poll for command from main
         sdata = self.sadapter.get_command()
         if sdata:
               self.sadapter.send_result('Response to scheduler from enforcer')

         # poll for command from network
         ndata = self.nadapter.get_command()
         if ndata:
               self.nadapter.send_result('Response to network from enforcer')