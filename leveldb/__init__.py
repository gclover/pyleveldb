
import os
import ctypes
import glob

path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'lib*.so')
for so in glob.glob(path):
	ctypes.cdll.LoadLibrary(so)

from leveldb_ import *

