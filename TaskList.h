#ifndef __TASKLIST_H__
#define __TASKLIST_H__

#include "Task.h"
#include <vector>

class TaskList {
	public:
		TaskList();

		bool updateTask(int progressed_time, int cur_time);
		void pushTask(Task task, int start_time);
		void sortList();

		Task& getTask(int i);
		Task& getTopTask();
		double getAvgResponseTime();
		int getWorstResponseTime();
		bool everyDone();
		int getWaitingSize();

		std::vector<Task> end_list;
	private:
		std::vector<Task> waiting_list;
};

#endif //__TASKLIST_H__