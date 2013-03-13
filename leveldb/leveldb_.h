#ifndef LEVELDB__H
#define LEVELDB__H

#include <string>

namespace leveldb
{

class LevelDB_ 
{
public:
	LevelDB_(std::string filename);
	~LevelDB_();

	std::string get(std::string key);
	bool put(std::string key, std::string value);
	bool del(std::string key);
private:
	leveldb::DB* db_;

};

}


#endif
