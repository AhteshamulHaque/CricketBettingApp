class LoggerProcess(Process):

   def __init__(self, ps, pn):
      super().__init__(name='logger')
      self.sadapter = ResponseAdapter(ps)
      self.nadapter = RequestAdapter(pn)

   def run(self):
      while True:

         # poll for command from main
         sdata = self.sadapter.get_command()
         if sdata:
               self.sadapter.send_result('Response to scheduler from logger')

         # poll for command from network
         ndata = self.nadapter.get_command()
         if ndata:
               self.nadapter.send_result('Response to network from logger')