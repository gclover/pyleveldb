
from distutils.core import setup
from setuptools import setup, find_packages
from Cython.Build import cythonize

extra_compile_args = ['-Wall', '-pedantic', '-I./deps/leveldb-1.9.0/include/','-shared', '-std=gnu99', '-fPIC', '-g', '-D_GNU_SOURCE']
extra_link_args = ['-L./leveldb', '-lleveldb', '-lsnappy', '-lpthread']

setup(
	name = "leveldb",
	version = '0.0.1',
	namespace_packages=[],
	packages = find_packages(),
	#zip_safe = False,

	description = "leveldb python binding",
	author = "gclover",
	author_email = "clover.gch@gmail.com",

	license = "",
	keywords = (),
	platforms = "Independant",
	url = "",

	ext_modules = cythonize(
		'leveldb/*.pyx',
		extra_compile_args = extra_compile_args,
		extra_link_args = extra_link_args
		)
)
