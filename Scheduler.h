#ifndef __SCHEDULER_H__
#define __SCHEDULER_H__

#include "TaskList.h"

class Scheduler {
	public:
		void RMScheduling(TaskList& task_list);
		void EDFScheduling(TaskList& task_list);
		void UserScheduling(TaskList& task_list);
	private:
};

#endif //__SCHEDULER_H__