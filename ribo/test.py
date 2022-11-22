from multiprocessing import Process, Pipe, Manager
from random import randint
import time

def worker(l):
   x = l
   x.append({'data': Pipe() })


if __name__ == '__main__':

   l = Manager().list()
   p = Process(target=worker, args=(l, ))
   p.start()

   time.sleep(2)