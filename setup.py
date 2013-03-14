
from setuptools import setup, find_packages
from Cython.Build import cythonize
from distutils.extension import Extension
from Cython.Distutils import build_ext

import os
import sys
import glob
import string
import shutil
import subprocess

snappy_path = glob.glob('deps/snappy*')[0]
leveldb_path = glob.glob('deps/leveldb*')[0]


def build_snappy():
	print 'build_snappy'
	conf_cmd = 'cd %s;./configure --enable-shared=false' % snappy_path
	make_cmd = 'cd %s;make' % snappy_path
	os.system(conf_cmd)
	os.system(make_cmd)

def build_leveldb():
	print 'build_leveldb'
	srclibs = "PLATFORM_LIBS=\n"
	destlibs = "PLATFORM_LIBS='-L../../%s/.libs'\n" % snappy_path
	detect_file = '%s/build_detect_platform' % leveldb_path
	content = open(detect_file, 'r').read()
	if srclibs in content:	
		changed_content = string.replace(content, srclibs, destlibs, 1)
		open(detect_file, 'w').write(changed_content)
	make_cmd = 'cd %s;make' % leveldb_path
	os.system(make_cmd)
	libso = glob.glob('deps/leveldb*/libleveldb.so.*')[0]
	destlibso = glob.glob('deps/leveldb*/')[0] + '/libleveldb.so'
	for dest in [destlibso]:
		if os.path.exists(dest):	
			os.unlink(dest)
		shutil.copy(libso, dest)


def main():
	if len(sys.argv) >= 2 and sys.argv[1] == 'build_deps':
		build_snappy()
		build_leveldb()
		return

    	print 'deleting generated files...'
	os.system('rm -rf build')
	os.system('rm -rf ext/leveldb.cpp')

	extra_compile_args = ['-I./%s/include/' % leveldb_path, '-shared']
	extra_link_args = ['-L%s' % leveldb_path, '-lleveldb', '-lpthread', '-Wl,--rpath=.']

	setup(
		name = "leveldb",
		version = '0.0.1',
		namespace_packages=[],
		packages = find_packages(),
		#zip_safe = False,

		data_files = [('', glob.glob('deps/leveldb*/libleveldb.so'))],

		description = "leveldb python binding",
		author = "gclover",
		author_email = "clover.gch@gmail.com",

		license = "",
		keywords = (),
		platforms = "Independant",
		url = "",

		cmdclass = {'build_ext' : build_ext},
		ext_modules = [
			Extension('leveldb_', 
				['ext/leveldb.pyx'] + glob.glob('ext/*.cpp'),
				language = 'c++',
				extra_compile_args = extra_compile_args,
				extra_link_args = extra_link_args
			)
		]
	)

if __name__ == '__main__':
	main()

