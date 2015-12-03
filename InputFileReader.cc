#include "InputFileReader.h"
#include <fstream>
#include <iostream>

using namespace std;

static void Tokenize(const string& str, 
	vector<string>& tokens, const string& delimiters = " ") {
	string::size_type lastPos = str.find_first_not_of(delimiters, 0);
	string::size_type pos = str.find_first_of(delimiters, lastPos);

	while (string::npos != pos || string::npos != lastPos) {
		tokens.push_back(str.substr(lastPos, pos - lastPos));
		lastPos = str.find_first_not_of(delimiters, pos);
		pos = str.find_first_of(delimiters, lastPos);
	}
}

vector<TaskForm>
InputFileReader::readFile(string file_name) throw (string)
{
	vector<TaskForm> res_v;
	ifstream input_f;
	string line;

	input_f.open(file_name, ifstream::in);

	while(!input_f.eof()) {
		getline(input_f, line);
		if (line.empty()) break;

		vector<string> tokens;
		Tokenize(line, tokens, " ");

		if (tokens.size() != 8) {
			string msg = "Arguments are missing!";
			throw msg;
		} else {
			bool periodic = (tokens[1].compare("true") == 0) ? true : false;
			int start_time = stoi(tokens[2]), request_time = stoi(tokens[3]);
			int period = stoi(tokens[4]), task_count = stoi(tokens[5]);
			int deadline = stoi(tokens[6]), priority = stoi(tokens[7]);
			TaskForm new_form(tokens[0], periodic, start_time, request_time,
				period, task_count, deadline, priority);

			res_v.push_back(new_form);
		}
	}

	return res_v;
}