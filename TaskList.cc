#include "TaskList.h"
#include <algorithm>

using namespace std;

TaskList::TaskList()
{
	waiting_list.clear();
	end_list.clear();
}

static bool
compTask(Task& task1, Task& task2)
{
	return task1.getPriority() < task2.getPriority() ? true :
			task1.getPriority() > task2.getPriority() ? false :
			task1.getStartTime() < task2.getStartTime();
}

void
TaskList::sortList()
{
	sort(waiting_list.begin(), waiting_list.end(), compTask);
}

bool
TaskList::updateTask(int progressed_time, int cur_time)
{
	if (!waiting_list.empty()) {
		Task& cur_task = waiting_list[0];
		cur_task.updateProgressedTime(progressed_time);

		if (cur_task.Done()) {
			Task temp_task = waiting_list[0];
			temp_task.setEndTime(cur_time);
			waiting_list.erase(waiting_list.begin());
			end_list.push_back(temp_task);
		}

		return true;
	}

	return false;
}

void
TaskList::pushTask(Task task, int start_time)
{
	task.setStartTime(start_time);
	waiting_list.push_back(task);
	this->sortList();
}

Task&
TaskList::getTask(int i)
{
	if (!waiting_list.empty() && i < waiting_list.size())
		return waiting_list[i];
}

Task&
TaskList::getTopTask()
{
	return this->getTask(0);
}

double
TaskList::getAvgResponseTime()
{
	double total_rt = 0;
	for (vector<Task>::iterator it = end_list.begin();
		it != end_list.end(); ++it) {
		total_rt += it->getResponseTime();
	}

	return total_rt / end_list.size();
}

int
TaskList::getWorstResponseTime()
{
	int worst = -1;
	for (vector<Task>::iterator it = end_list.begin();
		it != end_list.end(); ++it) {
		if (it->getResponseTime() > worst)
			worst = it->getResponseTime();
	}

	return worst;
}

bool
TaskList::everyDone()
{
	return waiting_list.empty();
}

int
TaskList::getWaitingSize()
{
	return waiting_list.size();
}