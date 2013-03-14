

import leveldb

db = leveldb.LevelDB('db1')
for i in range(10000):
	db.put('aaaaaaaaaaaaaa' + str(i), 'bbbbbbbbbbbbb')
	db.get('aaaaaaaaaaaaaa' + str(i))

