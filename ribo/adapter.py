TIMEOUT = 5

class RequestAdapter:
   def __init__(self, pipe):
      self.pipe = pipe
      
   def get_result(self, data):
      self.pipe.send(data)

      # if poll fails maybe the process is not alive
      if self.pipe.poll(TIMEOUT):
         return self.pipe.recv()


class ResponseAdapter:

   def __init__(self, pipe):
      self.pipe = pipe

      # preserve the order get_command -> send result
      self.buffered = False

   def get_command(self):
      if self.pipe.poll():
         self.buffered = True
         return self.pipe.recv()


   def send_result(self, data):
      if self.buffered:
         self.pipe.send(data)
         self.buffered = False
