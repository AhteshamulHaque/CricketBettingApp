import unittest, time
from multiprocessing import Pipe
from adapter import RequestAdapter, ResponseAdapter
from threading import Thread


class TestAdapters(unittest.TestCase):

   def setUp(self):
      p1, p2 = Pipe()
      self.req_adapter = RequestAdapter(p1)
      self.resp_adapter = ResponseAdapter(p2)

   def test_adapter(self):
      p1 = 