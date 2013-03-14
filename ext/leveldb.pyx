# distutils: language = c++
# distutils: sources = ext/leveldb_.cpp

from libcpp.string cimport string
from libcpp cimport bool

cdef extern from "leveldb_.h" namespace "leveldb":
	cdef cppclass LevelDB_:
		LevelDB_(string) except + 
		bool get(string, string&)
		bool put(string, string)
		bool delete_(string)
		string status()


cdef class LevelDB:
	cdef LevelDB_ *thisptr
	def __cinit__(self, string filename):
		self.thisptr = new LevelDB_(filename)
	def __dealloc__(self):
		del self.thisptr

	def get(self, key):
		cdef string value = ''
		res = self.thisptr.get(key, value)
		if res:
			return value
		else:
			return None

	def put(self, key, value):
		return self.thisptr.put(key, value)

	def delete(self, key):
		return self.thisptr.delete_(key)

