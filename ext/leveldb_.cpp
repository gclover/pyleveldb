
#include "leveldb_.h"

using namespace leveldb;

LevelDB_::LevelDB_(std::string filename)
{
	leveldb::Options options;
	options.create_if_missing = true;
	leveldb::Status status = leveldb::DB::Open(options, filename, &db_);
}

LevelDB_::~LevelDB_()
{}

std::string LevelDB_::get(std::string key)
{
	return "";
}

bool LevelDB_::put(std::string key, std::string value)
{
	return true;
}

bool LevelDB_::delete_(std::string key)
{
	return true;
}
