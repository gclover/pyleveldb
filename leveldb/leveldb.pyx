# distutils: language = c++
# distutils: sources = leveldb/leveldb_.cpp

cdef extern from "leveldb_.h" namespace "leveldb":
	cdef cppclass LevelDB_:
		LevelDB_(string) except + 
		string get(string)
		bool put(string, string)
		bool del(string)

cdef class LevelDB:
	cdef LevelDB_ *thisptr
	def __cinit__(self, string filename):
		self.thisptr = new LevelDB_(filename)
	def __dealloc__(self):
		del self.thisptr

	def get(self, key):
		return self.thisptr.get(key)

	def put(self, key, value):
		return self.thisptr.put(key, value)

	def delete(self, key):
		return self.thisptr.del(key)

