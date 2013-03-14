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

	bool get(std::string key, std::string& value);
	bool put(std::string key, std::string value);
	bool delete_(std::string key);
	
	std::string status();
private:
	leveldb::DB* db_;
	leveldb::Status status_;

};

}


#endif
