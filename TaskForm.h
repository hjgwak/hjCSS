#ifndef __TASKFORM_H__
#define __TASKFORM_H__

#include "Task.h"
#include <string>
#include <vector>
#include <utility>

#define TaskVector std::vector<std::pair<int, Task> >

class TaskForm {
	public:
		TaskForm() { };
		TaskForm(std::string new_name, bool periodic, int start_time,
			int request_time, int period = -1, int task_count = 1,
			int deadline = -1, int priority = -1);

		TaskVector makeTaskList();

	private:
		std::string task_name;
		bool periodic;
		int period;
		int task_count;
		int deadline;
		int start_time;
		int request_time;
		int priority;
};

#endif //__TASKFORM_H__