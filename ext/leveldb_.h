#ifndef LEVELDB__H
#define LEVELDB__H

#include <string>
#include <leveldb/db.h>

namespace leveldb
{

class LevelDB_ 
{
public:
	LevelDB_(std::string filename);
	~LevelDB_();

	std::string get(std::string key);
	bool put(std::string key, std::string value);
	bool delete_(std::string key);
private:
	leveldb::DB* db_;

};

}


#endif
