#include "TaskForm.h"

using namespace std;

TaskForm::TaskForm
(string new_name, bool periodic, int start_time,
	int request_time, int period /* -1 */, int task_count /* 1 */,
	int deadline /* -1 */, int priority /* -1 */)
{
	this->task_name = new_name;
	this->periodic = periodic;
	this->period = period;
	this->task_count = task_count;
	this->deadline = deadline;
	this->start_time = start_time;
	this->request_time = request_time;
	this->priority = priority;
}

TaskVector
TaskForm::makeTaskList()
{
	vector<pair<int, Task> > res_v;

	if (periodic) {
		for (int i = 0; i < task_count; ++i) {
			int task_start_time = start_time + i * period;
			Task new_task(task_name, request_time, task_start_time + period, priority);
		
			res_v.push_back(make_pair(task_start_time, new_task));
		}
	} else {
		Task new_task(task_name, request_time, deadline, priority);

		res_v.push_back(make_pair(start_time, new_task));
	}

	return res_v;
}