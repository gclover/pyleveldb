
#include "leveldb_.h"

using namespace leveldb;

LevelDB_::LevelDB_(std::string filename)
{
	leveldb::Options options;
	options.create_if_missing = true;
	status_ = leveldb::DB::Open(options, filename, &db_);
}

LevelDB_::~LevelDB_()
{
	if (db_)
		delete db_;
}

bool LevelDB_::get(std::string key, std::string& value)
{
	status_ = db_->Get(leveldb::ReadOptions(), key, &value);
	return status_.ok();
}

bool LevelDB_::put(std::string key, std::string value)
{
	status_ = db_->Put(leveldb::WriteOptions(), key, value);
	return status_.ok();	
}

bool LevelDB_::delete_(std::string key)
{
	status_ = db_->Delete(leveldb::WriteOptions(), key);
	return status_.ok();
}

std::string LevelDB_::status()
{
	return status_.ToString();
}

