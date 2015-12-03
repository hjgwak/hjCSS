#ifndef __INPUTFILEREADER_H__
#define __INPUTFILEREADER_H__

#include "TaskForm.h"
#include <vector>
#include <string>

class InputFileReader {
	public:
		std::vector<TaskForm> readFile(std::string file_name) throw (std::string);
	private:
};

#endif //__INPUTFILEREADER_H__